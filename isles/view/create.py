# isle/view/create.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from stores.models import Store

from isles.forms import IsleForm
from isles.models import Isle


class do(RequireUserMixin, generic.CreateView):
    """ Make a new Isle """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['store'] = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        context['back'] = context['store'].get_absolute_url()
        return context

    def form_valid(self, form):
        calling_store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        if Isle.objects.filter(user=self.request.user).filter(store=calling_store).count() > 64:
            messages.error(self.request,
                           'Sorry, this store already has the maximum number of isles.',
                           extra_tags='danger')
            return super(do, self).form_invalid(form)
        self.object = form.save(commit=False)
        self.object.store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        self.object.user = self.request.user
        messages.success(self.request, 'Isle %s added!' % form.cleaned_data['name'])
        log_form_valid(self, form, action='create')
        return super(do, self).form_valid(form)
