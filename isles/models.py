# isles/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from core.models import UltraModel

from stores.models import Store

class Isle(UltraModel):
    """    """
    name = models.PositiveSmallIntegerField(validators=[RegexValidator('^[0-9]{1,2}$')]) # I hate you.
    user = models.ForeignKey(User, related_name='isle')
    store = models.ForeignKey(Store, related_name='isle')
    #
    # Part of v4 refactor prep
    ## content = models.ManyToManyField(Item, related_name='isle')

    class Meta:
        unique_together = (("name", "store"),)
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('stores:detail', kwargs={'slug' : self.store.slug})

    def __str__(self):
        if len(self.notes) > 32:
            notes = '{}...'.format(self.notes[:32])
        else:
            notes = self.notes[:32]
        return '{} ({})'.format(self.name,notes)
