# lists/views.py

from django.views import generic
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from stores.models import Store

from .models import List
from .forms import ListCreateForm


class ListCreateView(generic.CreateView):
    """Make a new grocery list!"""
    form_class, model = ListCreateForm, List
    template_name = 'lists/index.html'
    this = 'G List'
    #

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.store = Store.objects.get(slug=self.kwargs.get('slug'))
        messages.success(self.request, '%s %s added!' % (self.this, form.cleaned_data['name'] ) )
        return super(ListCreateView, self).form_valid(form)

class ListListView(generic.DetailView):
    """Make a new grocery list!"""
    form_class, model = ListCreateForm, List
    template_name = 'lists/index.html'
    this = 'G List'
