# items/views.py

from __future__ import absolute_import

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from stores.models import Store
from isles.models import Isle

from .forms import ItemCreateForm
from .models import Item

class ItemCreateView(generic.CreateView):
    """ Make a new Item
    If the form that is embedded in storeDetailView is
    invalid it will redirect here, so give a standard
    form
    """
    form_class, model = ItemCreateForm, Item
    template_name = 'items/ItemCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        #
        # the 'cancel' button during isle create, there's a better way to do this but i ran out of s
        context['back'] = reverse_lazy('stores:detail', kwargs = {'slug' : self.kwargs.get('slug')})
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Item "%s" added!' % form.cleaned_data['name'])
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(generic.UpdateView):
    """Edit a Item"""
    form_class, model = ItemCreateForm, Item
    template_name = 'items/ItemUpdateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        return super(ItemUpdateView, self).form_valid(form)
