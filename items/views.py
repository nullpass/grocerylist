# items/views.py

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from core.mixins import RequireUserMixin, RequireOwnerMixin

from stores.models import Store
from isles.models import Isle

from .forms import EmbedtemForm, ItemForm
from .models import Item

class ItemIndex(RequireUserMixin, generic.ListView):
    """  """
    form_class, model = ItemForm, Item
    template_name = 'items/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(ItemIndex, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(store=Store.objects.get(slug=self.kwargs.get('slug')))
        return context


class ItemCreateView(RequireUserMixin, generic.CreateView):
    """ Make a new Item
    If the form that is embedded in storeDetailView is
    invalid it will redirect here, so give a standard
    form
    """
    form_class, model = EmbedtemForm, Item
    template_name = 'items/ItemCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        #
        # the 'cancel' button during isle create, there's a better way to do this but i ran out of s
        context['back'] = reverse_lazy('stores:detail', kwargs = {'slug' : self.kwargs.get('slug')})
        return context

    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this object is for """
        form = super(ItemCreateView, self).get_form(form_class)
        this_store = Store.objects.get(slug=self.kwargs.get('slug'))
        form.fields['from_isle'].queryset = Isle.objects.filter(store=this_store.id)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        self.object.user = self.request.user
        messages.success(self.request, 'Item "%s" added!' % form.cleaned_data['name'])
        self.object.save()
        ii = Isle.objects.get(id=self.object.from_isle.id)
        newitem = Item.objects.get(id=self.object.id)
        ii.content.add(newitem)
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """Edit an Item"""
    form_class, model = ItemForm, Item
    template_name = 'items/ItemUpdateView.html'

    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this object is for """
        form = super(ItemUpdateView, self).get_form(form_class)
        form.fields['from_isle'].queryset = Isle.objects.filter(store=self.object.store)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        #
        # Remove existing item->isle relation(s) in Isle.content
        old_relations = Isle.objects.filter(content=self.object.id).all()
        for this_relation in old_relations:
            this_relation.content.remove(self.object.id)
        #
        # Create one item->isle relation in Isle.content
        ii = Isle.objects.get(id=self.object.from_isle.id)
        ii.content.add(self.object.id)
        #
        messages.success(self.request, 'Changes saved!')
        return super(ItemUpdateView, self).form_valid(form)
