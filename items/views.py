# items/views.py

from __future__ import absolute_import

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from core.mixins import RenderdataMixin

from stores.models import Store
from isles.models import Isle

from .forms import ItemCreateForm
from .models import Item

class ItemCreateView(RenderdataMixin,generic.CreateView):
    """Make a new Item"""
    form_class, model = ItemCreateForm, Item
    template_name = 'items/ItemCreateView.html'
    this = 'Item'
    renderdata = { 'this' : this,
        'pagetitle' : 'Create %s' % this,
        'buttontext' : 'New %s' % this,
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, '%s %s added!' % (self.this, form.cleaned_data['name'] ) )
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(RenderdataMixin,generic.UpdateView):
    """Edit a Item"""
    form_class, model = ItemCreateForm, Item
    template_name = 'items/ItemUpdateView.html'
    this = 'Item'
    renderdata = { 'this' : this,
        'pagetitle' : 'Edit a %s' % this,
        'buttontext' : 'Save Changes',
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        return super(ItemUpdateView, self).form_valid(form)
