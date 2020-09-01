from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import MyUser
from tweet.models import Posts


def index(request):
    data = MyUser.objects.all()
    return render(request, "index.html", {'data': data})

def author(request, author_id):
    author_info = MyUser.objects.filter(id=author_id).first()
    post_list = Posts.objects.filter(author=author_info).order_by("-post_time")
    return render(request, "author.html", {"author": author_info, "posts": post_list})


def follow(request, author_id):
    request.user.follows.add(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

def unfollow(request, author_id):
    request.user.follows.remove(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

# https://stackoverflow.com/questions/58934300/best-implementation-follow-and-unfollow-in-django-rest-framework
    