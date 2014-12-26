# lists/views/create.py

import time

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from stores.models import Store
from items.models import Item

from lists.models import List, Tobuy
from lists.forms import EmbedListForm

class do(RequireUserMixin, generic.CreateView):
    form_class, model = EmbedListForm, List
    template_name = 'stores/StoreDetailView.html'

    def get(self, request, *args, **kwargs):
        """
        There is no regular CreateView for this model,
        we use an embedded form from StoreDetail; so
        only valid POST requests work on this view,
        if request.GET then redirect back to store.
        """
        store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        return redirect(store.get_absolute_url())

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.store = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        if List.objects.filter(user=self.request.user).count() > 25:
            messages.error(self.request, 'Sorry, you have too many lists already!', extra_tags='danger')
            return redirect(self.object.store.get_absolute_url())
        if not self.object.name:
            self.object.name = str( time.strftime("%a %b %d %Y", time.localtime()) )
        item_list = self.request.POST.getlist('content', False)
        if not item_list:
            messages.error(self.request, 'Failed to create new grocery list. No items were selected.', extra_tags='danger')
            return redirect(self.object.store.get_absolute_url())
        for this_item in item_list:
            # For each item the user checked create a new Tobuy object,
            # then link that new object to the List they are creating.
            item_match = get_object_or_404(Item, id=this_item)
            new_tobuy = Tobuy(name=item_match, quantity=1, user=self.request.user)
            new_tobuy.save()
            self.object.save()
            self.object.content.add(new_tobuy)
        log_form_valid(self, form, action='create')
        return super(do, self).form_valid(form)
