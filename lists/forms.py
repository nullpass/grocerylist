# lists/forms.py

from __future__ import absolute_import

from django.forms import ModelForm, CheckboxSelectMultiple

from . import models

class ListForm(ModelForm):
    class Meta:
        fields = (
            'name',
            'items',
            )
        model = models.List
        widgets = { 'items' : CheckboxSelectMultiple() }
