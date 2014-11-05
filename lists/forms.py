# lists/forms.py
from django import forms

from . import models

class ListForm(forms.ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            'line',
            )
        model = models.List


class ListUpdateForm(forms.ModelForm):
    """ """
    deleteme = forms.BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            'line',
            'done',
            'deleteme',
            )
        model = models.List


class LineForm(forms.ModelForm):
    """ """
    class Meta:
        fields = (
            'quantity',
            'item',
            )
        model = models.Line
        widgets = { 'item' : forms.CheckboxSelectMultiple() }
