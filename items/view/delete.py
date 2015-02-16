# items/view/delete.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_delete
from items.forms import ItemForm
from items.models import Item


class do(RequireUserMixin, RequireOwnerMixin, generic.DeleteView):
    """
    Delete an Item!
        Magically this seems to properly
        dispose of the through relationships.
    """
    form_class, model = ItemForm, Item
    template_name = 'item/ItemDeleteView.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse('index')
        if self.request.GET.get('next'):
            success_url = self.request.GET.get('next')
        log_delete(self)
        self.object.delete()
        messages.success(self.request, 'Item Deleted!')
        return redirect(success_url)
