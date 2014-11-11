# core/mixins.py

from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404

class RequireUserMixin(object):
    """ Require user logged in """
    mixin_messages = False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if self.mixin_messages:
                messages.warning(request, 'Unable to comply, please log in.')
            return redirect('{}?next={}'.format(reverse('auth3p'),request.path))
        return super(RequireUserMixin, self).dispatch(request, *args, **kwargs)


class RequireOwnerMixin(object):
    """ Require user owns object already """

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().user != self.request.user:
            raise Http404
        return super(RequireOwnerMixin, self).dispatch(request, *args, **kwargs)
