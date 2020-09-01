from django import forms
from tweet.models import Posts

class PostForm(forms.Form):
    content = forms.CharField(max_length=140)
    