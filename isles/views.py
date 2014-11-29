# isles/views.py

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from core.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from items.models import Item
from stores.models import Store

from .forms import IsleForm
from .models import Isle


class IsleCreateView(RequireUserMixin, generic.CreateView):
    """ Make a new Isle """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(IsleCreateView, self).get_context_data(**kwargs)
        context['store'] = Store.objects.get(slug=self.kwargs.get('slug'))
        return context

    def form_valid(self, form):
        calling_store = Store.objects.get(slug=self.kwargs.get('slug'))
        if Isle.objects.filter(user=self.request.user).filter(store=calling_store).count() > 64:
            messages.error(self.request, 'Sorry, this store already has the maximum number of isles.', extra_tags='danger')
            return super(IsleCreateView, self).form_invalid(form)
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        self.object.user = self.request.user
        messages.success(self.request, 'Isle %s added!' % form.cleaned_data['name'])
        log_form_valid(self, form)
        return super(IsleCreateView, self).form_valid(form)


class IsleUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """ Edit an Isle """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleUpdateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form)
        return super(IsleUpdateView, self).form_valid(form)
