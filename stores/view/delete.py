# stores/view/delete.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_delete

from stores.forms import StoreForm
from stores.models import Store

from items.models import Item
from isles.models import Isle
from lists.models import List


class do(RequireUserMixin, RequireOwnerMixin, generic.DeleteView):
    """
    Delete a Store!
        (as long as it's empty)
    """
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreDeleteView.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse('index')

        if Item.objects.filter(user=self.request.user).filter(store=self.object.id).count() == 0 \
        and Isle.objects.filter(user=self.request.user).filter(store=self.object.id).count() == 0 \
        and List.objects.filter(user=self.request.user).filter(store=self.object.id).count() == 0:
            log_delete(self)
            self.object.delete()
            messages.success(self.request, 'Store Deleted!')
            return redirect(success_url)
        else:
            messages.error(self.request, 'Unable to delete! There are still items, isles or grocery lists associated with this store.',extra_tags='danger')
            return redirect(self.object.get_absolute_url())
