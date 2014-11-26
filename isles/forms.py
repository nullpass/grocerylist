# isles/forms.py

from django.forms import ModelForm, TextInput

from .models import Isle

class IsleForm(ModelForm):
    """
    We don't present Isle.content here,
        that's updated with dirty magic
        while changing an item.
    """
    
    
    class Meta:
        fields = (
            'name',
            'notes',
            )
        model = Isle
        widgets = {
            'name' : TextInput(), 
            }
        
    def __init__(self, *args, **kwargs):
        super(IsleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['size'] = 1
        self.fields['name'].widget.attrs['maxlength'] = 2 # This is enforced by a regex in models. *sad panda*
        #self.fields['name'].help_text = "<em>(1-99)</em>"
        self.fields['name'].label = "Isle #"
        self.fields['notes'].widget.attrs['rows'] = 2
        self.fields['notes'].widget.attrs['cols'] = 64
        self.fields['notes'].label = "Description"
