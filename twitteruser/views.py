from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from twitteruser.models import MyUser
from tweet.models import Posts
from notification.models import Message
from twitteruser.forms import ProfileForm

@login_required
def index(request):
    data = MyUser.objects.all()
    following = request.user.follows.all()
    return render(request, "index.html", {'data': data, "following": following})

def author(request, username):
    if request.user.is_authenticated:
        author_info = MyUser.objects.filter(username=username).first()
        post_list = Posts.objects.filter(author=author_info).order_by("-post_time")
        following = author_info.follows.all()
        my_following = request.user.follows.all()
        pings = Message.objects.filter(receiver=request.user)
        return render(request, "author.html", {"author": author_info, "posts": post_list, "pings": pings, "following": following, "my_following": my_following})
    else:
        return HttpResponseRedirect('public')

def author_view(request, username):
    author_info = MyUser.objects.filter(username=username).first()
    post_list = Posts.objects.filter(author=author_info).order_by("-post_time")
    return render(request, "author.html", {"author": author_info, "posts": post_list})

@login_required
def author_list(request):
    user_list = MyUser.objects.all()
    my_following = request.user.follows.all()
    return render(request, "author_list.html", {"user_list": user_list, "my_following": my_following})

@login_required
def edit_author(request, username):
    edit = get_object_or_404(MyUser, username=username)
    if edit.username == request.user.username:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('author', username)
        else:
            form = ProfileForm(instance=edit)
        return render(request, 'generic_form.html', {'form': form})
    else: return HttpResponseForbidden("You do not have permission to edit this post")

@login_required
def remove_author(request, username):
    profile = get_object_or_404(MyUser, username=username)
    if profile.username == request.user.username:
        profile.delete()
        return redirect("homepage")
    else: return HttpResponseForbidden("You do not have permission to remove this profile")
    
@login_required
def follow(request, author_id):
    request.user.follows.add(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def unfollow(request, author_id):
    request.user.follows.remove(MyUser.objects.get(id=author_id))
    return HttpResponseRedirect(reverse('homepage'))

"""
# https://stackoverflow.com/questions/58934300/best-implementation-follow-and-unfollow-in-django-rest-framework

# username as url: https://stackoverflow.com/questions/3013098/django-username-in-url-instead-of-id/16258084

Some of the resources used for uploading photo feature:
https://www.geeksforgeeks.org/python-uploading-images-in-django/
https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial
https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
"""