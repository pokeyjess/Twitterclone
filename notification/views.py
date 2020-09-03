from django.shortcuts import render, HttpResponseRedirect, reverse
from notification.models import Message
from twitteruser.models import MyUser

def notifications(request):
    notification = Message.objects.filter(receiver=request.user)
    return render(request, "notifications.html", {'notification': notification})

    # https://stackoverflow.com/questions/32687461/how-to-create-a-user-to-user-message-system-using-django
    
    # Thanks to Matt for helping me tweak this so it works properly!

