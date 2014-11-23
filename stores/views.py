# stores/views.py

from django.views import generic
from django.contrib import messages
from django.http import Http404

from core.mixins import RequireUserMixin, RequireOwnerMixin

from items.forms import ItemCreateForm
from items.models import Item

from isles.models import Isle

from lists.models import List
from lists.forms import ListForm

from .forms import StoreForm
from .models import Store


class StoreIndex(RequireUserMixin, generic.TemplateView):
    """ The default view for /s/ ; a list of your stores """
    form_class, model = StoreForm, Store
    template_name = 'stores/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(StoreIndex, self).get_context_data(**kwargs)
        context['stores'] = Store.objects.filter(user=self.request.user).values('slug', 'name')
        context['user'] = self.request.user
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
        # Items that belong to this store.
        #context['inventory'] = Item.objects.filter(store=self.object.id).order_by('isle', 'name')
        # Isles that belong to this store
        context['isles'] = Isle.objects.filter(store=self.object.id)
        #local_isles = Isle.objects.filter(store=self.object.id)
        #if local_isles:
        #    context['isles'] = local_isles
        #    context['ItemCreateForm'] = ItemCreateForm()
            #context['ItemCreateForm'].fields['isle'].queryset = local_isles
            #context['ItemCreateForm'].fields['isle'].initial = local_isles[0]
        #
        # My non-deleted Grocery Lists that reference this store, newest first
        context['related_lists'] = List.objects.filter(store=self.object.id).filter(deleteme=False).order_by('-pk')
        context['fours'] = [4,8,12,16,20,24,28,32,36,40,44]
        return context


class StoreUpdateView(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """Edit a Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreUpdateView.html'

    def form_valid(self, form):
        messages.success(self.request, 'Changes saved!')
        return super(StoreUpdateView, self).form_valid(form)


class StoreCreateView(RequireUserMixin, generic.CreateView):
    """Make a new Store"""
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreCreateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, 'Store "{}" added!'.format(form.cleaned_data['name']) )
        return super(StoreCreateView, self).form_valid(form)
