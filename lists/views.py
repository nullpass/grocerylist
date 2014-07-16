# lists/views.py

import decimal

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from stores.models import Store
from isles.models import Isle

from .models import List
from .forms import ListCreateForm


class ListCreateView(generic.CreateView):
    """Make a new grocery list!"""
    form_class, model = ListCreateForm, List
    template_name = 'lists/index.html'
    this = 'G List'
    #

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        messages.success(self.request, '%s %s added!' % (self.this, form.cleaned_data['name'] ) )
        return super(ListCreateView, self).form_valid(form)

class ListDetailView(generic.DetailView):
    """ List a List List, Lists of Listing """
    form_class, model = ListCreateForm, List
    template_name = 'lists/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['localisles'] = Isle.objects.filter(store=self.object.store).order_by('name')
        context['total_cost'] = decimal.Decimal(0.00)
        for X in self.object.items.all():
            context['total_cost'] += X.price
        return context
