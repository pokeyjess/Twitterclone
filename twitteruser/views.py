from django.shortcuts import render
from twitteruser.models import MyUser
from tweet.models import Posts


def index(request):
    data = MyUser.objects.all()
    return render(request, "index.html", {'data': data})

def author(request, author_id):
    author_info = MyUser.objects.filter(id=author_id).first()
    post_list = Posts.objects.filter(author=author_info).order_by("-post_time")
    return render(request, "author.html", {"author": author_info, "posts": post_list})
