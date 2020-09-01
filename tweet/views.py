from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Posts
from tweet.forms import PostForm

def index(request):
    post_list = Posts.objects.all().order_by('-post_time')
    return render(request, "index.html", {"post_list": post_list})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(content=data['content'], author=request.user)
            return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, "generic_form.html", {"form": form})

