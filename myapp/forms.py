from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        error_messages={'required': 'The username field is required.'},
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            })
    )

    email = forms.EmailField(
        error_messages = {'required':'The Email field is required'},
        widget = forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            })
    )

    password1 = forms.CharField(
        error_messages= {'required':'The Password1 is required'},
        widget = forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            })
    )

    password2 = forms.CharField(
        error_messages={'required':'The password is required'},
        widget = forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            })
    )

class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required':'The Username is required'},
        widget = forms.TextInput(
            attrs={
                "placeholder" : "User name",
                "class" : "form-control"
            })
    )

    password = forms.CharField(
        error_messages= {'required':'The Password is required'},
        widget = forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
            })
    )