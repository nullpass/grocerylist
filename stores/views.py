# stores/views.py

from __future__ import absolute_import

from itertools import izip

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from core.mixins import RenderdataMixin

from items.forms import ItemCreateForm
from items.models import Item

from isles.models import Isle

from lists.models import List
from lists.forms import ListCreateForm

from .forms import StoreForm
from .models import Store

link_box = [
    ('Store List',       reverse_lazy('index')),
    #('Isles',        'isles:index'),
    #('Items',        'isles:index'),
]

class Index(generic.TemplateView):
    """
    The default view for /stores/
    """
    form_class, model = StoreForm, Store
    template_name = 'stores/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['link_box'] = link_box
        context['this']     = ' -THIS- '
        #
        context['sectiontitle'] = 'Stores'
        context['pagetitle']    = 'page title'
        try:
            context['stores'] = Store.objects.all().values('slug', 'name')
        except Store.DoesNotExist:
            context['stores'] = None
        return context


class StoreCreateView(RenderdataMixin,generic.CreateView):
    """Make a new Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreCreateView.html'
    this = 'Store'
    renderdata = { 'this' : this,
        'pagetitle' : 'Create %s' % this,
        'buttontext' : 'New %s' % this,
        'link_box' : link_box,
    }

    def form_valid(self, form):
        messages.success(self.request, '%s %s added!' % (self.this, form.cleaned_data['name'] ) )
        return super(StoreCreateView, self).form_valid(form)


class StoreDetailView(RenderdataMixin,generic.DetailView):
    """View a Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(StoreDetailView, self).get_context_data(**kwargs)
        context['pagetitle'] = self.object.name
        context['this'] = 'Store'
        context['buttontext'] = 'Edit %s' % context['this']
        context['link_box'] = link_box
        #
        context['ListCreateForm'] = ListCreateForm()
        context['ListCreateForm'].fields['items'].queryset = Item.objects.filter(store=self.object.id)
        #
        context['Items'] = Item.objects.filter(store=self.object.id)
        context['ItemForm'] = ItemCreateForm()
        #
        # Only show isles that belong to this store.
        temp = Isle.objects.filter(store=self.object.id).order_by('name')
        context['isles'] = temp
        context['ItemForm'].fields['isle'].queryset = temp
        try:
            context['ItemForm'].fields['isle'].initial = temp[0]
        except IndexError:
            # "dey aint no isles yet, fool!" --Sr. Bug Reporter
            pass
        #
        # Everything about this is SO STUPID- but I love it!
        try:
            context['next'] = Store.objects.get(pk=self.object.id + 1)
        except Store.DoesNotExist:
            context['next'] = None
        try:
            context['prev'] = Store.objects.get(pk=self.object.id - 1)
        except Store.DoesNotExist:
            context['prev'] = None
        #
        #
        return context


class StoreUpdateView(RenderdataMixin,generic.UpdateView):
    """Edit a Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreUpdateView.html'
    this = 'Store'
    renderdata = { 'this' : this,
        'pagetitle' : 'Edit a %s' % this,
        'buttontext' : 'Save Changes',
        'link_box' : link_box,
    }

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved!')
        return super(StoreUpdateView, self).form_valid(form)
