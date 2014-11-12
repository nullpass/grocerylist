# recent/views.py

from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from core.mixins import RequireUserMixin

from . import models

class RecentIndex(RequireUserMixin, generic.ListView):
    model = models.Log
    template_name = 'recent/index.html'
    
    def get_queryset(self):
        return models.Log.objects.filter(user=self.request.user).all()


class RecentDetailView(RequireUserMixin, generic.DetailView):
    model = models.Log
    template_name = 'recent/LogDetail.html'

"""

recent_patterns = patterns('',
    #
    # /recent/
    url(r'^$', RecentIndex.as_view(), name='index'), 
    #
    # /recent/<log pk>/
    url(r'^(?P<pk>\d+)/$', RecentDetailView.as_view(), name='detail'),
)

"""