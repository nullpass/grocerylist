# isles/forms.py
from __future__ import absolute_import
#
from django.forms import ModelForm

from . import models

class IsleForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'notes',
            )
        model = models.Isle
