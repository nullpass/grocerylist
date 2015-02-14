# stores/views.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from stores.forms import StoreForm
from stores.models import Store


class do(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """Edit a Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreUpdateView.html'

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form, action='update')
        return super(do, self).form_valid(form)
