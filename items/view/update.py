# items/views/update.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid
from isles.models import Isle
from items.forms import ItemForm
from items.models import Item


class do(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """Edit an Item"""
    form_class, model = ItemForm, Item
    template_name = 'item/ItemUpdateView.html'

    def get_context_data(self, **kwargs):
        """
        if ?next is set then use that for the Cancel button
        Otherwise cancel == url of store this item belongs to.
        """
        context = super(do, self).get_context_data(**kwargs)
        context['back'] = self.object.store.get_absolute_url()
        if self.request.GET.get('next'):
            self.object.save()
            context['back'] = self.request.GET.get('next')
        return context


    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this object is for """
        form = super(do, self).get_form(form_class)
        form.fields['from_isle'].queryset = Isle.objects.filter(user=self.request.user).filter(store=self.object.store)
        form.initial['from_isle'] = get_object_or_404(Isle, content=self.object.id)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        #
        # Remove existing item->isle relation(s) in Isle.content
        for this_relation in Isle.objects.filter(user=self.request.user).filter(content=self.object.id):
            this_relation.content.remove(self.object.id)
        #
        # Create one item->isle relation in Isle.content
        # ( make Item.from_isle equal Isle.content )
        new_relation = get_object_or_404(Isle, id=self.object.from_isle.id)
        new_relation.content.add(self.object.id)
        #
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form, action='update')
        if self.request.GET.get('next'):
            self.object.save()
            return redirect(self.request.GET.get('next'))
        return super(do, self).form_valid(form)
