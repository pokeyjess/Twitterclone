from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from tweet.models import Posts
from tweet.forms import PostForm
from twitteruser.models import MyUser
from notification.models import Message
import re

@login_required
def index(request):
    post_list = Posts.objects.all().order_by('-post_time')
    # user_list = MyUser.objects.all().order_by('username')
    pings = Message.objects.filter(receiver=request.user)
    return render(request, "index.html", {"post_list": post_list, "pings": pings})

@login_required
def post_form_view(request):
    pings = Message.objects.filter(receiver=request.user)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Posts.objects.create(content=data['content'], author=request.user)
            if '@' in data['content']:
                recipient = re.findall(r'@(\w+)', data.get('content'))
                for receipt in recipient:
                    message = Message.objects.create(msg_content=tweet, receiver=MyUser.objects.get(username=receipt))      
            return HttpResponseRedirect(reverse('homepage'))
    form = PostForm()
    return render(request, "generic_form.html", {"form": form, "pings": pings})

def post_detail(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Posts, id=post_id)
        pings = Message.objects.filter(receiver=request.user)
        return render(request, 'post_detail.html', {'post': post, 'pings': pings})
    else:
        return HttpResponseRedirect('public')

def public_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def edit_post(request, post_id):
    pings = Message.objects.filter(receiver=request.user)
    edit = get_object_or_404(Posts, id=post_id)
    if edit.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=edit)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
                return redirect('post', post_id)
        else:
            form = PostForm(instance=edit)
        return render(request, 'generic_form.html', {'form': form, 'pings': pings})
    else: 
        return HttpResponseForbidden("You do not have permission to edit this post")

@login_required
def remove_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if post.author == request.user:
        post.delete()
        return redirect("homepage")
    else:
        return HttpResponseForbidden("You do not have permission to remove this post")

@login_required
def up_vote(request, post_id):
    vote = Posts.objects.get(id=post_id)
    vote.total_votes += 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))
    
@login_required
def down_vote(request, post_id):
    vote = Posts.objects.get(id=post_id)
    vote.total_votes -= 1
    vote.save()
    return redirect(request.META.get('HTTP_REFERER'))

def votes(request):
    post_list = Posts.objects.all().order_by('-total_votes')
    return render(request, "index.html", {"post_list": post_list})

