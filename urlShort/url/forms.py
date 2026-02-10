from django import forms

class Url(forms.Form):
    url = forms.URLField(
        label="Enter URL",
        widget=forms.URLInput(attrs={
            'placeholder': 'https://example.com'
        })
    )
