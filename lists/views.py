# lists/views.py
from __future__ import absolute_import

import decimal
import time

from django.views import generic
from django.contrib import messages

from stores.models import Store
from isles.models import Isle
from items.models import Item

from .models import List
from .forms import ListForm, ListUpdateForm

class ListIndex(generic.TemplateView):
    """ The default view for /mylists/ ; a list of lists """
    form_class, model = ListForm, List
    template_name = 'lists/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListIndex, self).get_context_data(**kwargs)
        context['mylists'] = List.objects.all()
        context['stores'] = Store.objects.all()
        return context


class ListCreateView(generic.CreateView):
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
        context['store'] = Store.objects.get(slug=self.kwargs.get('slug'))
        return context

    def form_valid(self, form):
        """
        By default we do not present form.name
        to the user in StoreDetailView, so if it is
        empty then set it to Today.
        """
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        if not self.object.name:
            self.object.name = str( time.strftime("%a %b %d %Y", time.localtime()) )
        return super(ListCreateView, self).form_valid(form)


class ListDetailView(generic.DetailView):
    """ View a grocery list in a mobile-friendly way """
    form_class, model = ListForm, List
    template_name = 'lists/ListDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['localisles'] = Isle.objects.filter(store=self.object.store).order_by('name')
        context['total_cost'] = decimal.Decimal(0.00)
        for X in self.object.items.all():
            context['total_cost'] += X.price
        return context


class ListUpdateView(generic.UpdateView):
    """ Edit a grocery list """
    form_class, model = ListUpdateForm, List
    template_name = 'lists/ListUpdateView.html'

    def get_context_data(self,  **kwargs):
        """ Include all items that belong to the store found in the URL """
        context = super(ListUpdateView, self).get_context_data(**kwargs)
        self.form_class.base_fields['items'].queryset = Item.objects.filter(store=self.object.store.id)
        return context


    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.cleaned_data['delete_me']:
            self.success_url = self.object.store.get_absolute_url()
            messages.success(self.request, 'List "%s" deleted!' % self.object.name )
        return super(ListUpdateView, self).form_valid(form)
