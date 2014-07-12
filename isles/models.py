# isles/models.py

from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy

from core.models import UltraModel

from stores.models import Store

class Isle(UltraModel):
    """
    """
    name = models.CharField(max_length=2)
    description = models.TextField(max_length=1024)
    store = models.ForeignKey(Store, related_name='isle')

    class Meta:
        unique_together = (("name", "store"),)

    def get_absolute_url(self):
        return reverse('stores:detail', kwargs={'slug' : self.store.slug})
