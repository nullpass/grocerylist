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
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('done'))
                this_tobuy.in_cart = True
                this_tobuy.save()
                resval = '{0}#{1}'.format(
                    reverse('lists:detail', kwargs={'pk' : kwargs.get('pk')}),
                    this_tobuy.id
                    )
                return redirect(resval)
            except Exception as e:
                print(e)
        elif request.GET.get('undo'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('undo'))
                this_tobuy.in_cart = False
                this_tobuy.save()
                resval = '{0}#{1}'.format(
                    reverse('lists:detail', kwargs={'pk' : kwargs.get('pk')}),
                    this_tobuy.id
                    )
                return redirect(resval)

            except Exception as e:
                print(e)
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
