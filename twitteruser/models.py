from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class MyUser(AbstractUser):
    bio = models.TextField(null=True, blank=True, verbose_name="About Me")
    job_title = models.CharField(max_length=80, null=True, blank=True, default="", verbose_name="What I Do")
    joined_date = models.DateField(auto_now_add=True)
    follows = models.ManyToManyField("self", symmetrical=False)

# https://stackoverflow.com/questions/16613013/model-self-dependency-one-to-many-field-implementation/16614136#16614136

# https://stackoverflow.com/questions/2029295/django-datefield-default-options

# https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/
