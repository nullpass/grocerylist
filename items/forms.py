# items/forms.py

from django.forms import ModelForm, CheckboxSelectMultiple

from . import models

class ItemCreateForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'price',
            )
        model = models.Item
        #widgets = { 'item' : CheckboxSelectMultiple() }


class ItemForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'price',
            'from_isle',
            )
        model = models.Item
        widgets = { 'from_isle' : CheckboxSelectMultiple() }