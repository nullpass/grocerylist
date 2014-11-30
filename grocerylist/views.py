# grocerylist/views.py

from collections import OrderedDict

from django.views import generic
from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy

from lists.models import List, Tobuy
from stores.models import Store

from .mixins import RequireUserMixin

class LogoutView(generic.RedirectView):
    """ Blindly log out any request that hits this url with a GET """
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, 'You have logged out!')
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(generic.TemplateView):
    """
    Show third-party authentication page
    """
    template_name = 'home/auth3p.html'


class HelpView(generic.TemplateView):
    """
    Attempt to show help based on what's in the URL
    """
    template_name = 'home/help.html'


class HomeView(RequireUserMixin, generic.TemplateView):
    """
    The default view for /
    A list of your stores
        and non-deleted lists
    """
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['threes'] = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
        context['content'] = OrderedDict()
        for this_store in Store.objects.filter(user=self.request.user).order_by('-modified'):
            context['content'][this_store] = List.objects.filter(user=self.request.user).filter(store=this_store).order_by('modified')
        return context

class MaintenanceView(RequireUserMixin, generic.TemplateView):
    """
    """
    template_name = 'home/help.html'

    def get(self, request, *args, **kwargs):
        messages.info(self.request, 'Maintenance')
        if self.request.user.is_staff:
            #
            # Report orphaned Tobuy objects.
            # OG: http://stackoverflow.com/questions/10609699/efficiently-delete-orphaned-m2m-objects-tags-in-django
            orphans = list()
            for this in Tobuy.objects.filter(
                pk__in=list(
                    set(Tobuy.objects.values_list('pk', flat=True))
                    -
                    set(List.content.through.objects.values_list('tobuy', flat=True))
                    )
                ):
                orphans.append(this.id)
                #this.delete()
            if orphans:
                messages.warning(self.request, 'Tobuy orphans: {}'.format(orphans))
        return super(MaintenanceView, self).get(self, request, *args, **kwargs)
