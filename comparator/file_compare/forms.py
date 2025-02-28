from django import forms
from django.forms import widgets

from .models import Compare, DoctoPdf, PdftoDoc


class CompareForm(forms.ModelForm):
    class Meta:
        model = Compare
        fields = ('generic_file', 'file_to_compare')
        # widget = {
        #     'generic_file' : forms.TextInput(attrs = {'class': 'form-control'}),
        #     'file_to_compare' : forms.TextInput(attrs = {'class': 'form-control'}),
            
        # }
        
class DoctoPdfForm(forms.ModelForm):
    class Meta:
        model = DoctoPdf
        fields = ('word_file',)
        
class PdftoDocForm(forms.ModelForm):
    class Meta:
        model = PdftoDoc
        fields = ('pdf_file',)
        