# lists/view/delete.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_delete

from lists.forms import ListForm
from lists.models import List


class do(RequireUserMixin, RequireOwnerMixin, generic.DeleteView):
    """
    Delete a List!
        By default this does leave Tobuy orphans, so I've
        added a delete override to handle it.
    """
    form_class, model = ListForm, List
    template_name = 'lists/ListDeleteView.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.object.store.get_absolute_url()
        for tobuy in self.object.content.all():
            tobuy.delete()
        log_delete(self)
        self.object.delete()
        messages.success(self.request, 'List Deleted!')
        return redirect(success_url)
