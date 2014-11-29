# recent/views.py

from django.views import generic

from grocerylist.mixins import RequireUserMixin, RequireOwnerMixin

from .models import Log

class RecentIndex(RequireUserMixin, generic.ListView):
    model = Log
    template_name = 'recent/index.html'
    
    def get_queryset(self):
        return Log.objects.filter(user=self.request.user).order_by('-pk').all()[:50]


class RecentDetailView(RequireUserMixin, RequireOwnerMixin, generic.DetailView):
    model = Log
    template_name = 'recent/LogDetail.html'
