# lists/views.py
import decimal
import time
from collections import OrderedDict

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.models import modelformset_factory

from core.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from stores.models import Store
from isles.models import Isle
from items.models import Item

from .models import List, Tobuy
from .forms import ListForm, ListUpdateForm, EmbedListForm, TobuyForm

class ListIndex(RequireUserMixin, generic.TemplateView):
    """ The default view for /mylists/ ; a list of lists """
    form_class, model = ListForm, List
    template_name = 'lists/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListIndex, self).get_context_data(**kwargs)
        context['mylists'] = List.objects.filter(user=self.request.user).filter(deleteme=False)
        context['stores'] = Store.objects.filter(user=self.request.user).order_by('pk')
        return context


class ListCreateView(RequireUserMixin, generic.CreateView):
    """    """
    form_class, model = EmbedListForm, List
    template_name = 'lists/ListCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(ListCreateView, self).get_context_data(**kwargs)
        context['store'] = Store.objects.filter(user=self.request.user).filter(slug=self.kwargs.get('slug')).get()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.store = Store.objects.filter(user=self.request.user).filter(slug=self.kwargs.get('slug')).get()
        if not self.object.name:
            self.object.name = str( time.strftime("%a %b %d %Y", time.localtime()) )
        #
        # You're a messy night coder, but this end works, fix it Thursday.
        item_list = self.request.POST.getlist('content', False)
        if not item_list:
            messages.error(self.request, 'Failed to create new grocery list. No items were selected.', extra_tags='danger')
            return redirect(self.object.store.get_absolute_url())
        for this_item in item_list:
            """
            For each item the user checked create a new Tobuy object,
            then link that new object to the List they are creating.
            """
            item_match = Item.objects.get(id=this_item)
            new_tobuy = Tobuy(name=item_match, quantity=1, user=self.request.user)
            new_tobuy.save()
            self.object.save()
            self.object.content.add(new_tobuy)
        log_form_valid(self, form)
        return super(ListCreateView, self).form_valid(form)


class ListDetailView(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    """ View a grocery list in a mobile-friendly way """
    form_class, model = ListForm, List
    template_name = 'lists/ListDetailView.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('done'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('done'))
                this_tobuy.in_cart = True
                this_tobuy.save()
                return redirect(reverse('lists:detail',kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        elif request.GET.get('undo'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('undo'))
                this_tobuy.in_cart = False
                this_tobuy.save()
                return redirect(reverse('lists:detail',kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        # all-else
        return super(ListDetailView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['isles'] = Isle.objects.filter(store=self.object.store).order_by('name').all()
        d = OrderedDict()
        context['total_cost'] = decimal.Decimal(0.00)
        for this in context['isles']:
            d[this] = list()
        for item in self.object.content.all():
            context['total_cost'] += ( item.name.price * item.quantity )
            d[item.name.from_isle].append(item)
        context['d'] = d
        return context

class ListUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """
    
    """
    form_class, model = ListUpdateForm, List
    template_name = 'lists/ListUpdateView.html'
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('inc'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('inc'))
                this_tobuy.quantity += 1
                this_tobuy.save()
                return redirect(reverse('lists:update',kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        elif request.GET.get('dec'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('dec'))
                this_tobuy.quantity -= 1
                this_tobuy.save()
                if this_tobuy.quantity < 1:
                    this_tobuy.delete()
                return redirect(reverse('lists:update',kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        elif request.GET.get('insert'):
            try:
                # Get item from db
                item_match = Item.objects.filter(user=self.request.user).get(id=request.GET.get('insert'))
                #
                # Create a new Tobuy object with that item
                new_tobuy = Tobuy(name=item_match, quantity=1, user=self.request.user)
                new_tobuy.save()
                #
                # find current List
                this_list = List.objects.filter(user=self.request.user).get(id=kwargs.get('pk'))
                #
                # Attach new Item to List.content
                this_list.content.add(new_tobuy)
                this_list.save()
                #
                # Go back to /mylists/PK/update
                return redirect(reverse('lists:update',kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        # all-else
        return super(ListUpdateView, self).get(self, request, *args, **kwargs)


    
    def get_context_data(self, **kwargs):
        """
        Generate a list of items that belong to this list's store
            but that are not already in this list.
        
        """
        context = super(ListUpdateView, self).get_context_data(**kwargs)
        #
        # New iterable for Items we can add to this Grocery List
        context['can_add'] = list()
        #
        # What we currently have in this Grocery List
        local_tobuys = self.object.content.values_list('name', flat=True)
        #
        # If item in inventory not in this Grocery List, add to 'can_add'
        for this_item in Item.objects.filter(store=self.object.store).filter(user=self.request.user).all():
            if this_item.id not in local_tobuys:
                context['can_add'].append(this_item)
        #
        return context

    def form_valid(self, form):
        """
        
        """
        self.object = form.save(commit=False)
        if form.cleaned_data['deleteme']:
            self.success_url = self.object.store.get_absolute_url()
            self.object.deleteme = True
            messages.success(self.request, 'List "%s" deleted!' % self.object.name )
        log_form_valid(self, form)
        return super(ListUpdateView, self).form_valid(form)
