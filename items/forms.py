# items/forms.py

from django.forms import ModelForm

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


class ItemForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'price',
            )
        model = models.Item
