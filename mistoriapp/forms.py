from django import forms

class formForm(forms.Form):
    name=forms.CharField(max_length=40, required=True)
    topic=forms.CharField(max_length=200, required=True)
    audience=forms.CharField(max_length=40, required=True)
    keyword=forms.CharField(max_length=100, required=True)
