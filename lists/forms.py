# lists/forms.py
from django.forms import ModelForm, CheckboxSelectMultiple, BooleanField

from .models import List

class ListForm(ModelForm):
    """ """
    class Meta:
        fields = (
            'name',
            #'content',
            )
        model = List
        widgets = { 'content' : CheckboxSelectMultiple() }

class ListUpdateForm(ModelForm):
    """ """
    deleteme = BooleanField(required=False)
    class Meta:
        fields = (
            'name',
            #'content',
            'done',
            'deleteme',
            )
        model = List
        widgets = { 'content' : CheckboxSelectMultiple() }
        
        
        
class EmbedListForm(ModelForm):
    """ """
    content = CheckboxSelectMultiple()
    class Meta:
        fields = (
            'name',
            )
        model = List
