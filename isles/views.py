# isles/views.py

from __future__ import absolute_import

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from core.mixins import RenderdataMixin

from stores.models import Store

from .forms import IsleForm
from .models import Isle

class IsleCreateView(generic.CreateView):
    """Make a new Isle"""
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleCreateView.html'

    def get_context_data(self, **kwargs):
        context = super(IsleCreateView, self).get_context_data(**kwargs)
        #
        # the 'cancel' button during isle create, there's a better way to do this but i ran out of s
        context['back'] = reverse_lazy('stores:detail', kwargs = {'slug' : self.kwargs.get('slug')})
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, '%s %s added!' % (self.this, form.cleaned_data['name'] ) )
        return super(IsleCreateView, self).form_valid(form)


class IsleUpdateView(RenderdataMixin,generic.UpdateView):
    """Edit a Isle"""
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleUpdateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        return super(IsleUpdateView, self).form_valid(form)

    
