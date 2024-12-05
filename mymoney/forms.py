from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm (UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'register-container',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'register-container',
            'placeholder': 'Email Address'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'register-container',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'register-container',
            'placeholder': 'Confirm Password'
        })
