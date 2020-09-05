from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class MyUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name="About Me")
    joined_date = models.DateField(auto_now_add=True)
    follows = models.ManyToManyField("self", symmetrical=False)

# https://stackoverflow.com/questions/16613013/model-self-dependency-one-to-many-field-implementation/16614136#16614136

# https://stackoverflow.com/questions/2029295/django-datefield-default-options
