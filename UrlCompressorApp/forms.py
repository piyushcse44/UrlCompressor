# forms.py
from django import forms

class CompressorForm(forms.Form):
    long_url = forms.URLField(max_length=200)
    custom_url = forms.CharField(max_length=200)
    custom_back_half = forms.CharField(max_length=200)

    def validate_custom_back_half(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters.")
        return username
