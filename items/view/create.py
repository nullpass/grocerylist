# items/view/create.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from stores.models import Store
from isles.models import Isle

from items.forms import ItemForm
from items.models import Item


class do(RequireUserMixin, generic.CreateView):
    """ Make a new Item
    If the form that is embedded in storeDetailView is
    invalid it will redirect here, so give a standard
    form
    """
    form_class, model = ItemForm, Item
    template_name = 'item/ItemCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['store'] = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        context['back'] = context['store'].get_absolute_url()
        return context

    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this object is for """
        form = super(do, self).get_form(form_class)
        this_store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        form.fields['from_isle'].queryset = Isle.objects.filter(user=self.request.user).filter(store=this_store.id)
        return form

    def form_valid(self, form):
        """
        Enforce
            limits
            object ownership
        Bark
        Log
        
        """
        if Item.objects.filter(user=self.request.user).count() > 256:
            messages.error(self.request, 'Sorry, you have too many items already!', extra_tags='danger')
            return super(do, self).form_invalid(form)
        #
        self.object = form.save(commit=False)
        self.object.store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        self.object.user = self.request.user
        #
        # Update the other side of the item-isle relationship.
        self.object.save()
        target_isle = get_object_or_404(Isle, user=self.request.user, id=self.object.from_isle.id)
        newitem = get_object_or_404(Item, user=self.request.user, id=self.object.id)
        target_isle.content.add(newitem)
        #
        messages.success(self.request, 'Item "%s" added!' % form.cleaned_data['name'])
        log_form_valid(self, form, action='create')
        return super(do, self).form_valid(form)
