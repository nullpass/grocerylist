# lists/views/index.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid

from stores.models import Store

from lists.models import List, Tobuy
from lists.forms import ListForm


class do(RequireUserMixin, generic.TemplateView):
    """
    This now shows all grocery lists that exist that belong to store kwargs.slug
    
    If user is staff this also checks for orphaned Tobuy objects.
        The check itself does not filter by user.
    """
    form_class, model = ListForm, List
    template_name = 'lists/index.html'

    def get_context_data(self, **kwargs):
        context = super(do, self).get_context_data(**kwargs)
        context['store'] = get_object_or_404(Store, user=self.request.user, slug=self.kwargs.get('slug'))
        context['lists'] = List.objects.filter(user=self.request.user).filter(store=context['store']).filter(deleteme=False).order_by('-modified')
        return context
