# isles/view/delete.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_delete

from isles.forms import IsleForm
from isles.models import Isle

from items.models import Item
from lists.models import List


class do(RequireUserMixin, RequireOwnerMixin, generic.DeleteView):
    """
    Delete an Isle!
        (as long as it's empty)
    """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleDeleteView.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.object.store.get_absolute_url()
        #
        if Item.objects.filter(user=self.request.user).filter(isle=self.object.id).count() == 0 \
        and self.object.content.all().count() == 0:
            log_delete(self)
            self.object.delete()
            messages.success(self.request, 'Isle Deleted!')
        else:
            messages.error(self.request,
                           'Unable to delete! There are still items linked to this isle.',
                           extra_tags='danger')
        #
        return redirect(success_url)
