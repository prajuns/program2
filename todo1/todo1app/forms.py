from django import forms
from . models import todo1

class todo1form(forms.ModelForm):
    class Meta:
        model=todo1
        fields=['name','priority','date']