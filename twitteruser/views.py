from django.shortcuts import render
from twitteruser.models import MyUser

def index(request):
    data = MyUser.objects.all()
    return render(request, "index.html", {'data': data})
