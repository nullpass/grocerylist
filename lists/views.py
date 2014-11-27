# lists/views.py
import decimal
import time
from collections import OrderedDict

from django.views import generic
from django.contrib import messages

from core.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from stores.models import Store
from isles.models import Isle
from items.models import Item

from .models import List, Tobuy
from .forms import ListForm, ListUpdateForm, EmbedListForm

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
            messages.error(self.request, 'No items were selected.', extra_tags='danger')
            return super(ListCreateView, self).form_invalid(form)
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

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['isles'] = Isle.objects.filter(store=self.object.store).order_by('name').all()
        d = OrderedDict()
        context['total_cost'] = decimal.Decimal(0.00)
        for this in context['isles']:
            d[this] = list()
        for item in self.object.content.all():
            context['total_cost'] += item.name.price
            d[item.name.from_isle].append(item)
        context['d'] = d
        return context


class ListUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """ Edit a grocery list """
    form_class, model = ListUpdateForm, List
    template_name = 'lists/ListUpdateView.html'
    
    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this list is for """
        form = super(ListUpdateView, self).get_form(form_class)
        form.fields['content'].queryset = Item.objects.filter(store=self.object.store)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.cleaned_data['deleteme']:
            self.success_url = self.object.store.get_absolute_url()
            self.object.deleteme = True
            messages.success(self.request, 'List "%s" deleted!' % self.object.name )
        log_form_valid(self, form)
        return super(ListUpdateView, self).form_valid(form)
