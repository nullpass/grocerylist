# lists/views/update.py

from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid
from items.models import Item
from lists.models import List, Tobuy
from lists.forms import ListUpdateForm


class do(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    form_class, model = ListUpdateForm, List
    template_name = 'lists/ListUpdateView.html'
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('inc'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('inc'))
                this_tobuy.quantity += 1
                this_tobuy.save()
                retval = '{0}#{1}'.format(
                    reverse('lists:update', kwargs={'pk' : kwargs.get('pk')}),
                    this_tobuy.id
                    )
                return redirect(retval)
            except Exception as e:
                print(e)
        elif request.GET.get('dec'):
            try:
                this_tobuy = Tobuy.objects.filter(user=self.request.user).get(id=request.GET.get('dec'))
                this_tobuy.quantity -= 1
                this_tobuy.save()
                retval = '{0}#{1}'.format(
                    reverse('lists:update', kwargs={'pk' : kwargs.get('pk')}),
                    this_tobuy.id
                    )
                if this_tobuy.quantity < 1:
                    this_tobuy.delete()
                return redirect(retval)
            except Exception as e:
                print(e)
        elif request.GET.get('insert'):
            try:
                # Get item from db
                item_match = Item.objects.filter(user=self.request.user).get(id=request.GET.get('insert'))
                #
                # Create a new Tobuy object with that item
                new_tobuy = Tobuy(name=item_match, quantity=1, user=self.request.user)
                new_tobuy.save()
                #
                # find current List
                this_list = List.objects.filter(user=self.request.user).get(id=kwargs.get('pk'))
                #
                # Attach new Item to List.content
                this_list.content.add(new_tobuy)
                this_list.save()
                #
                # Go back to /mylists/PK/update
                return redirect(reverse('lists:update', kwargs={'pk' : kwargs.get('pk')}))
            except Exception as e:
                print(e)
        # all-else
        return super(do, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Generate a list of items that belong to this list's store
        # but that are not already in this list.
        context = super(do, self).get_context_data(**kwargs)
        #
        # New iterable for Items we can add to this Grocery List
        context['can_add'] = list()
        #
        # What we currently have in this Grocery List
        local_tobuys = self.object.content.values_list('name', flat=True)
        #
        # If item in inventory not in this Grocery List, add to 'can_add'
        for this_item in Item.objects.filter(user=self.request.user).filter(store=self.object.store):
            if this_item.id not in local_tobuys:
                context['can_add'].append(this_item)
        #
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.cleaned_data['deleteme']:
            return redirect(reverse('lists:delete', kwargs={ 'pk' : self.object.pk }))
        log_form_valid(self, form, action='update')
        return super(do, self).form_valid(form)
