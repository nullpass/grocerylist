# stores/views.py

from django.views import generic

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from items.forms import EmbedItemForm
from items.models import Item
from isles.models import Isle
from lists.models import List
from stores.forms import StoreForm
from stores.models import Store


class do(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    """
    View a Store
    and allow user to create a grocery list for that store
    """
    form_class, model = StoreForm, Store
    template_name = 'stores/StoreDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['inventory'] = Item.objects.filter(user=self.request.user).filter(store=self.object.id).count()
        g = List.objects.filter(user=self.request.user).filter(store=self.object.id).filter(done=False).count()
        if g > 0:
            context['glist_count'] = g
        context['isles'] = Isle.objects.filter(user=self.request.user).filter(store=self.object.id)
        #
        if context['isles']:
            context['EmbedItemForm'] = EmbedItemForm()
            context['EmbedItemForm'].fields['from_isle'].queryset = Isle.objects.filter(user=self.request.user).filter(store=self.object.id)
            context['EmbedItemForm'].fields['from_isle'].initial = context['isles'][0]
        #
        # Fat-belly hack for div rows
        context['fours'] = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]
        return context
