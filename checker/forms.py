from django import forms
from .models import Document

class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)

class TextForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea, max_length=2000)
