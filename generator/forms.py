# generator/forms.py
from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(min_value=6, max_value=32, initial=12, label="Password Length")
    include_uppercase = forms.BooleanField(required=False, label="Include Uppercase Letters")
    include_numbers = forms.BooleanField(required=False, label="Include Numbers")
    include_symbols = forms.BooleanField(required=False, label="Include Special Characters")
