# lists/models.py
from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.models import UltraModel

from items.models import Item
from stores.models import Store

class List(UltraModel):
    """    """
    name = models.CharField(max_length=64, blank=True, null=True) # in views defaults to self.created
    user = models.ForeignKey(User, related_name='list')
    store = models.ForeignKey(Store, related_name='list')
    #
    done = models.BooleanField(default=False)
    deleteme = models.BooleanField(default=False)
    #
    #
    # v4 refactor, change to Isle
    #content = models.ManyToManyField(Item, related_name='list')

    def get_absolute_url(self):
        return reverse('lists:detail', kwargs={'pk' : self.pk})
