from django import forms
from tweet.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["content"]


'''
    content = forms.CharField(max_length=140)
    post_time = forms.DateTimeField(default=timezone.now)
    author = forms.

    post_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
'''