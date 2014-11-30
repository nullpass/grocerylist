# stores/views.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from stores.forms import StoreForm
from stores.models import Store


class do(RequireUserMixin, generic.CreateView):
    """Make a new Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreCreateView.html'

    def form_valid(self, form):
        """
        limit checking
        object ownership
        barking
        logging
        """
        if Store.objects.filter(user=self.request.user).count() > 32:
            messages.error(self.request, 'Sorry, you have too many stores already!', extra_tags='danger')
            return super(do, self).form_invalid(form)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, 'Store "{}" added!'.format(form.cleaned_data['name']) )
        log_form_valid(self, form)
        return super(do, self).form_valid(form)
