# human/views.py
from socket import gethostbyname

from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from core.mixins import RequireAnonMixin, RequireUserMixin

class LoginView(RequireAnonMixin, generic.FormView):
    """ log in page, require no user logged in """
    form_class, model = AuthenticationForm, User
    template_name = 'human/LoginView.html'
    success_url = reverse_lazy('human:index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                messages.success(self.request, 'Welcome back!')
                login(self.request, user)
                if self.request.GET.get('next'):
                    self.success_url = self.request.GET['next']
                return super(LoginView, self).form_valid(form)
        return super(LoginView, self).form_invalid(form)


class LogoutView(generic.RedirectView):
    """ Blindly log out any request that hits this url with a GET """
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(self.request, 'You have logged out!')
        return super(LogoutView, self).get(request, *args, **kwargs)
