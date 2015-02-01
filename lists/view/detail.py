# lists/views/detail.py

import decimal
from collections import OrderedDict

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from isles.models import Isle

from lists.models import List, Tobuy
from lists.forms import ListForm

class do(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    form_class, model = ListForm, List
    template_name = 'lists/ListDetailView.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('done'):
            this_tobuy = get_object_or_404(Tobuy, user=self.request.user, id=request.GET.get('done'))
            this_tobuy.in_cart = True
            this_tobuy.save()
            #
            # If all items are in cart then mark grocery list as done
            parent = this_tobuy.list.get()
            if parent.content.all().filter(in_cart=False).count() is 0:
                parent.done = True
                parent.save()
            #
            retval = '{0}#{1}'.format(
                reverse('lists:detail', kwargs={'pk' : kwargs.get('pk')}),
                this_tobuy.id
                )
            return redirect(retval)
        elif request.GET.get('undo'):
            this_tobuy = get_object_or_404(Tobuy, user=self.request.user, id=request.GET.get('undo'))
            this_tobuy.in_cart = False
            this_tobuy.save()
            #
            # When putting an item back make sure grocery list is NOT set to done.
            parent = this_tobuy.list.get()
            parent.done = False
            parent.save()
            #
            retval = '{0}#{1}'.format(
                reverse('lists:detail', kwargs={'pk' : kwargs.get('pk')}),
                this_tobuy.id
                )
            return redirect(retval)
        # all-else
        return super(do, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['isles'] = Isle.objects.filter(user=self.request.user).filter(store=self.object.store).order_by('name')
        context['d'] = OrderedDict()
        context['total_cost'] = decimal.Decimal(0.00)
        for this in context['isles']:
            context['d'][this] = list()
        for item in self.object.content.all():
            context['total_cost'] += ( item.name.price * item.quantity )
            context['d'][item.name.from_isle].append(item)
        return context
