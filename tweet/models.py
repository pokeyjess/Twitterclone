from django.db import models
from django.utils import timezone
from twitteruser.models import MyUser

class Posts(models.Model):
    content = models.CharField(max_length=140)
    post_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)

