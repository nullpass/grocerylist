# lists/views.py
import decimal
import time

from django.views import generic
from django.contrib import messages

from core.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from stores.models import Store
from isles.models import Isle
from items.models import Item

from .models import List
from .forms import ListForm, ListUpdateForm

class ListIndex(RequireUserMixin, generic.TemplateView):
    """ The default view for /mylists/ ; a list of lists """
    form_class, model = ListForm, List
    template_name = 'lists/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListIndex, self).get_context_data(**kwargs)
        context['mylists'] = List.objects.filter(user=self.request.user).filter(deleteme=False)
        context['stores'] = Store.objects.filter(user=self.request.user)
        return context


class ListCreateView(RequireUserMixin, generic.CreateView):
    """
    Make a new grocery list!
    
    LCV is presented in two different ways. First it is included in StoreDetailView to let a user
    easily create a list while viewing a store. Second it has its on CreateView template which is
    usually used if there is an error in the form included on StoreDetailView (for example if a
    user hits 'genereate list' without checking any items.)
    """
    form_class, model = ListForm, List
    template_name = 'lists/ListCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(ListCreateView, self).get_context_data(**kwargs)
        context['store'] = Store.objects.filter(user=self.request.user).filter(slug=self.kwargs.get('slug')).get()
        return context

    def form_valid(self, form):
        """
        By default we do not present form.name
        to the user in StoreDetailView, so if it is
        empty then set it to Today.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.store = Store.objects.filter(user=self.request.user).filter(slug=self.kwargs.get('slug')).get()
        if not self.object.name:
            self.object.name = str( time.strftime("%a %b %d %Y", time.localtime()) )
        log_form_valid(self, form)
        return super(ListCreateView, self).form_valid(form)


class ListDetailView(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    """ View a grocery list in a mobile-friendly way """
    form_class, model = ListForm, List
    template_name = 'lists/ListDetailView.html'

    def get_context_data(self, **kwargs):
        """ Sort list by isle and calculate total price. """
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['local_isles'] = list()
        context['total_cost'] = decimal.Decimal(0.00)
        for this in self.object.content.order_by('isle').all():
            context['total_cost'] += this.price
            if this.isle not in context['local_isles']:
                context['local_isles'].append(this.isle)
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
