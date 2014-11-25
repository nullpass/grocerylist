# items/forms.py

from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect

from . import models

class EmbedtemForm(ModelForm):
    """ """
    
    class Meta:
        fields = (
            'name',
            'price',
            'from_isle',
            )
        model = models.Item


class ItemForm(ModelForm):
    """ """
    
    class Meta:
        fields = (
            'name',
            'price',
            'from_isle',
            )
        model = models.Item
        widgets = { 'from_isle' : RadioSelect() }
