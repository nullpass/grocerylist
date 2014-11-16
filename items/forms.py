# items/forms.py

from django.forms import ModelForm, CheckboxSelectMultiple

from . import models

class ItemCreateForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'price',
            'isle',
            )
        model = models.Item
        widgets = { 'item' : CheckboxSelectMultiple() }


class ItemForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'price',
            'isle',
            )
        model = models.Item
        widgets = { 'item' : CheckboxSelectMultiple() }