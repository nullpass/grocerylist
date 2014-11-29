# stores/models.py
from __future__ import absolute_import

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator

from grocerylist.models import UltraModel

class Store(UltraModel):
    """
    
    """
    name = models.CharField(max_length=128, validators=[RegexValidator('^[A-Za-z0-9a-z\.,\- ]+$')])
    user = models.ForeignKey(User, related_name='store')
    address = models.CharField(max_length=1024, validators=[RegexValidator('^[A-Za-z0-9a-z\.,\- ]+$')], unique=True)
    slug = models.SlugField(max_length=256, blank=True)

    #class Meta:
    #    unique_together = (("name", "address"),)

    def save(self, *args, **kwargs):
        temp = '%s %s ' % (self.name, self.address)
        self.slug = slugify(temp)
        super(Store, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('stores:detail', kwargs={'slug' : self.slug})
