from django.db import models
from django.utils import timezone
from twitteruser.models import MyUser
from tweet.models import Posts


class Message(models.Model):
    receiver = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="receiver")
    msg_content = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)

# https://stackoverflow.com/questions/32687461/how-to-create-a-user-to-user-message-system-using-django
