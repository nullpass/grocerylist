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
        context['mylists'] = List.objects.filter()
        try:
            context['stores'] = List.objects.all()
        except Store.DoesNotExist:
            context['stores'] = None
        return context


class ListCreateView(generic.CreateView):
    """Make a new grocery list!"""
    form_class, model = ListForm, List
    template_name = 'lists/ListCreateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        if not self.object.name:
            self.object.name = str( time.strftime("%a %b %d %Y", time.localtime()) )
        return super(ListCreateView, self).form_valid(form)


class ListDetailView(generic.DetailView):
    """ List a List List, Lists of Listing """
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
        context = super(ListUpdateView, self).get_context_data(**kwargs)
        #
        # Ensure you only show items that exist in the store for which this list belongs.
        self.form_class.base_fields['items'].queryset = Item.objects.filter(store=self.object.store.id)
        return context
