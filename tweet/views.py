from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from tweet.models import Posts
from tweet.forms import PostForm
from twitteruser.models import MyUser
from notification.models import Message
import re

@login_required
def index(request):
    post_list = Posts.objects.all().order_by('-post_time')
    user_list = MyUser.objects.all().order_by('display_name')
    return render(request, "index.html", {"post_list": post_list, "user_list": user_list})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Posts.objects.create(content=data['content'], author=request.user)
            if '@' in data['content']:
                recipient = re.findall(r'@(\w+)', data.get('content'))
                for receipt in recipient:
                    message = Message.objects.create(msg_content=tweet, receiver=MyUser.objects.get(display_name=receipt))      
            return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, "generic_form.html", {"form": form})

def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, 'post_detail.html', {'post': post})
