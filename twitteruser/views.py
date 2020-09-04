from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import MyUser
from tweet.models import Posts
from notification.models import Message

@login_required
def index(request):
    data = MyUser.objects.all()
    following = request.user.follows.all()
    return render(request, "index.html", {'data': data, "following": following})

def author(request, display_name):
    author_info = MyUser.objects.filter(display_name=display_name).first()
    post_list = Posts.objects.filter(author=author_info).order_by("-post_time")
    pings = Message.objects.order_by('-created_at')
    return render(request, "author.html", {"author": author_info, "posts": post_list, "pings": pings})

@login_required
def follow(request, author_id):
    request.user.follows.add(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def unfollow(request, author_id):
    request.user.follows.remove(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

# https://stackoverflow.com/questions/58934300/best-implementation-follow-and-unfollow-in-django-rest-framework

# username as url: https://stackoverflow.com/questions/3013098/django-username-in-url-instead-of-id/16258084

