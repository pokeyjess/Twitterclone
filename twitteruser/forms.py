from django import forms
from twitteruser.models import MyUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['bio']
        