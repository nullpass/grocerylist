# isle/view/update.py

from django.views import generic
from django.contrib import messages

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin
from recent.functions import log_form_valid
from isles.forms import IsleForm
from isles.models import Isle


class do(RequireUserMixin, RequireOwnerMixin, generic.UpdateView):
    """ Edit an Isle """
    form_class, model = IsleForm, Isle
    template_name = 'isles/IsleUpdateView.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.success_url = self.object.store.get_absolute_url()
        messages.success(self.request, 'Changes saved!')
        log_form_valid(self, form, action='update')
        return super(do, self).form_valid(form)
