# from django import forms
# from django.contrib.auth.models import Group
# from django.utils.translation import ugettext_lazy as _




# class LoginForm(forms.Form):
#     username = forms.CharField(required=True, max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )