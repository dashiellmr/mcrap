from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label='Enter your notes', max_length=256)