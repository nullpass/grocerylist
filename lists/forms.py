# lists/forms.py
from django.forms import ModelForm, CheckboxSelectMultiple, BooleanField

from .models import List, Tobuy


class ListForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            )
        model = List
        widgets = {'content': CheckboxSelectMultiple() }


class ListUpdateForm(ModelForm):
    """ """
    deleteme = BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            'done',
            'deleteme',
            )
        model = List

        
class EmbedListForm(ModelForm):
    """ """
    content = CheckboxSelectMultiple()
    class Meta:
        fields = (
            'name',
            )
        model = List


class TobuyForm(ModelForm):
    class Meta:
        fields = (
            'quantity',
        )
        model = Tobuy
