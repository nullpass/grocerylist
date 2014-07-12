# items/forms.py

from __future__ import absolute_import

from django.forms import ModelForm

from . import models

class ItemCreateForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'price',
            'isle',
            'notes',
            )
        model = models.Item


class ItemForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'price',
            'selected',
            )
        model = models.Item
