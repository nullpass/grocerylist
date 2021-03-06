# recent/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Log(models.Model):
    """ """
    user = models.ForeignKey(User, related_name='log')
    model_name = models.CharField(max_length=1024, blank=True, null=True)
    view_name = models.CharField(max_length=1024, blank=True, null=True)
    object_name = models.CharField(max_length=1024, blank=True, null=True)
    when = models.DateTimeField(auto_now_add=True)  # now()
    verbose = models.CharField(max_length=1024, blank=True, null=True)    # request.POST
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.user, self.view_name, self.object_name)

    def get_absolute_url(self):
        return reverse('recent:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-when']
