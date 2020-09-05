from django import forms
from tweet.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["content"]
