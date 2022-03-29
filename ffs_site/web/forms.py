from pkgutil import ImpImporter
from django import forms
from django.contrib.auth.models import User

class registerForm(forms.Form):
    username = forms.CharField(max_length=30, label="username")
    password = forms.CharField(max_length=50, min_length=6, label="password", widget=forms.PasswordInput)
    email = forms.EmailField(label="E-Mail eintragen")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Diesen Username gibt es schon!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Diese E-Mail gibt es schon!')
        return email

class loginForm(forms.Form):
    username = forms.CharField(max_length=30, label="username")
    password = forms.CharField(max_length=50, min_length=6, label="password", widget=forms.PasswordInput)