# isles/models.py
import re

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from grocerylist.models import UltraModel
from items.models import Item
from stores.models import Store


class Isle(UltraModel):
    """    """
    name = models.CharField(max_length=2, validators=[RegexValidator('^[A-Za-z0-9a-z]+$')])
    user = models.ForeignKey(User, related_name='isle')
    store = models.ForeignKey(Store, related_name='isle')
    content = models.ManyToManyField(Item, blank=True, related_name='isle')

    class Meta:
        unique_together = (("name", "store"),)
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('stores:detail', kwargs={'slug': self.store.slug})

    def __str__(self):
        if len(self.notes) > 32:
            notes = '{0}...'.format(self.notes[:32])
        else:
            notes = self.notes[:32]
        return '{0} ({1})'.format(self.name, notes)

    def save(self, *args, **kwargs):
        """
        Now that Isle.name is a str instead of an int
            either I add a leading zero to numerically-named
            Isles or I have to write a natural sorting function
            and implement it in a brazzillion places.
            Guess which route I've gone.
        """
        if re.search('^[0-9]$', self.name):
            self.name = '0{0}'.format(self.name)
        super(Isle, self).save(*args, **kwargs)
