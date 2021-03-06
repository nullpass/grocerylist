# stores/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

from grocerylist.models import UltraModel
from grocerylist.functions import UltraSlug


class Store(UltraModel):
    """
    
    """
    name = models.CharField(max_length=128, validators=[RegexValidator("^[A-Za-z0-9a-z\.,'\- ]+$")])
    user = models.ForeignKey(User, related_name='store')
    address = models.CharField(max_length=1024, validators=[RegexValidator('^[A-Za-z0-9a-z\.,\- ]+$')], unique=True)
    slug = models.SlugField(max_length=256, blank=True, unique=True)

    def save(self, *args, **kwargs):
        temp = '{0} {1}'.format(self.name, self.address)
        self.slug = UltraSlug(temp, self)
        super(Store, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('stores:detail', kwargs={'slug' : self.slug})
