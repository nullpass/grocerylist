# items/view/index.py

from django.views import generic
from django.shortcuts import get_object_or_404

from grocerylist.mixins import RequireUserMixin
from stores.models import Store
from items.forms import ItemForm
from items.models import Item


class do(RequireUserMixin, generic.ListView):
    """  """
    form_class, model = ItemForm, Item
    template_name = 'item/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['store'] = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        context['items'] = Item.objects.filter(user=self.request.user).filter(store=context['store'])
        return context
