# lists/forms.py

from __future__ import absolute_import

from django.forms import ModelForm

from . import models

class ListCreateForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'items',
            )
        model = models.List
