# isles/views.py

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from core.mixins import RequireUserMixin, RequireOwnerMixin

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
        #
        # the 'cancel' button during isle create, there's a better way to do this but i ran out of s
        context['back'] = reverse_lazy('stores:detail', kwargs = {'slug' : self.kwargs.get('slug')})
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        self.success_url = self.object.store.get_absolute_url()
        self.object.user = self.request.user
        messages.success(self.request, 'Isle %s added!' % form.cleaned_data['name'])
        return super(IsleCreateView, self).form_valid(form)


class IsleUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """ Edit an Isle """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleUpdateView.html'

    def get_form(self, form_class):
        """ Limit choice of items to those that exist in the store this object is for """
        form = super(IsleUpdateView, self).get_form(form_class)
        this_store = Store.objects.get(slug=self.kwargs.get('slug'))
        form.fields['content'].queryset = Item.objects.filter(store=this_store.id)
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        return super(IsleUpdateView, self).form_valid(form)
