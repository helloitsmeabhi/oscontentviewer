# forms.py
from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
