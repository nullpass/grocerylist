# lists/models.py
from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.models import UltraModel

from items.models import Item
from stores.models import Store

class Line(UltraModel):
    """
    2014.11
    
    
    """
    quantity = models.IntegerField(default=0)
    item = models.ForeignKey(Item, related_name='line') # ( name and price of item ) 
    

class List(UltraModel):
    """
    name of list
    created date [um]
    M2M pointing to items
    
    """
    name = models.CharField(max_length=64, blank=True, null=True) # in views defaults to self.created
    user = models.ForeignKey(User, related_name='list')
    store = models.ForeignKey(Store, related_name='list')
    items = models.ManyToManyField(Item, related_name='list')
    done = models.BooleanField(default=False)
    delme = models.BooleanField(default=False)
    lines = models.ManyToManyField(Line, related_name='list')

    def get_absolute_url(self):
        return reverse('lists:detail', kwargs={'pk' : self.pk})
