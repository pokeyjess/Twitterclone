from django import forms
from twitteruser.models import MyUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
