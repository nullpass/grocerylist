# stores/views.py

from django.views import generic
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin

from recent.functions import log_form_valid

from items.forms import EmbedItemForm, ItemForm
from items.models import Item

from isles.models import Isle

from lists.models import List
from lists.forms import ListForm

from .forms import StoreForm
from .models import Store


class StoreIndex(RequireUserMixin, generic.TemplateView):
    """ The default view for / ; a list of your stores """
    form_class, model = StoreForm, Store
    template_name = 'stores/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(StoreIndex, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.filter(user=self.request.user).order_by('pk').values('slug', 'name')
        return context


class StoreDetailView(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    """
    View a Store
    and allow user to create a grocery list for that store
    """
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(StoreDetailView, self).get_context_data(**kwargs)
        #
        # Count of Items that belong to this store.
        context['inventory'] = Item.objects.filter(store=self.object.id).count()
        #
        # Isles that belong to this store
        local_isles = Isle.objects.filter(store=self.object.id)
        if local_isles:
            context['isles'] = local_isles
            context['EmbedItemForm'] = EmbedItemForm()
            context['EmbedItemForm'].fields['from_isle'].queryset = Isle.objects.filter(store=self.object.id)
            context['EmbedItemForm'].fields['from_isle'].initial = local_isles[0]
        #
        # My non-deleted Grocery Lists that reference this store, newest first
        #context['related_lists'] = List.objects.filter(store=self.object.id).filter(deleteme=False).order_by('-pk')
        #
        # Fat-belly hack for div rows
        context['fours'] = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248, 252, 256, 260, 264, 268, 272, 276, 280, 284, 288, 292, 296, 300, 304, 308, 312, 316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 356, 360, 364, 368, 372, 376, 380, 384, 388, 392, 396, 400]
        return context


class StoreUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """Edit a Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreUpdateView.html'

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form)
        return super(StoreUpdateView, self).form_valid(form)


class StoreCreateView(RequireUserMixin, generic.CreateView):
    """Make a new Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreCreateView.html'

    def form_valid(self, form):
        if Store.objects.filter(user=self.request.user).count() > 32:
            messages.error(self.request, 'Sorry, you have too many stores already!', extra_tags='danger')
            return super(StoreCreateView, self).form_invalid(form)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, 'Store "{}" added!'.format(form.cleaned_data['name']) )
        log_form_valid(self, form)
        return super(StoreCreateView, self).form_valid(form)
