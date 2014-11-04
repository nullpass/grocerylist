# lists/forms.py
from django import forms

from . import models

class ListForm(forms.ModelForm):
    class Meta:
        fields = (
            'name',
            'line',
            )
        model = models.List
        #widgets = { 'items' : forms.CheckboxSelectMultiple() }



class ListUpdateForm(forms.ModelForm):
    deleteme = forms.BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            'line',
            'done',
            'deleteme',
            )
        model = models.List
        #widgets = { 'items' : forms.CheckboxSelectMultiple() }

class LineForm(forms.ModelForm):
    class Meta:
        fields = (
            'quantity',
            'item',
            )
        model = models.Line
