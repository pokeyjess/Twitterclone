from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notification.models import Message

@login_required
def notifications(request):
    notification = Message.objects.filter(receiver=request.user)
    for view in notification:
        view.delete()
    return render(request, "notifications.html", {'notification': notification})

    # https://stackoverflow.com/questions/32687461/how-to-create-a-user-to-user-message-system-using-django
    
    # Thanks to Matt for helping me tweak this so it works properly!

# https://stackoverflow.com/questions/38807551/python-django-how-to-delete-an-instance-automatically-after-an-action
# https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/
