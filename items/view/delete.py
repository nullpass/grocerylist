# items/views/delete.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from isles.models import Isle

from lists.models import Tobuy

from items.forms import ItemForm
from items.models import Item


class do(RequireUserMixin, RequireOwnerMixin, generic.DeleteView):
    """    Delete an Item!
        Magically this seems to properly
        dispose of the through relationships.
    """
    form_class, model = ItemForm, Item
    template_name = 'item/ItemDeleteView.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Item Deleted!')
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return reverse_lazy('index')
