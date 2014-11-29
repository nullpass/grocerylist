# grocerylist/views.py

from django.views import generic
from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy


class LogoutView(generic.RedirectView):
    """ Blindly log out any request that hits this url with a GET """
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, 'You have logged out!')
        return super(LogoutView, self).get(request, *args, **kwargs)


class HelpView(generic.TemplateView):
    """
    Attempt to show help based on what's in the URL
    """
    template_name = 'help.html'
