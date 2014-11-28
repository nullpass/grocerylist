# lists/models.py
from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.models import UltraModel

from items.models import Item
from stores.models import Store

class List(UltraModel):
    """
    Functionally just a container for Tobuy lines with
        some extra spice and ownership.
    """
    name = models.CharField(max_length=64, blank=True, null=True) # in views defaults to self.created
    user = models.ForeignKey(User, related_name='list')
    store = models.ForeignKey(Store, related_name='list')
    #
    done = models.BooleanField(default=False)
    deleteme = models.BooleanField(default=False)
    #
    content = models.ManyToManyField('Tobuy', related_name='list')

    def get_absolute_url(self):
        return reverse('lists:detail', kwargs={'pk' : self.pk})

class Tobuy(UltraModel):
    """
    'To Buy'
    These are the lines you make your list out of. 
    """
    name = models.ForeignKey(Item, related_name='tobuy')
    quantity = models.PositiveIntegerField(max_length=32, default=1)
    user = models.ForeignKey(User, related_name='tobuy')
    in_cart = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

"""
class Archive(UltraModel):
    #
    # Once a List is done, it gets converted to a string and stored here
    name = models.CharField(max_length=10240)
"""
