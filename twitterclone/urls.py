"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from twitteruser.views import index, author, follow, unfollow, edit_author, remove_author, author_view, author_list, find_list
from authentication.views import signup_view, login_view, logout_view
from tweet.views import index, post_form_view, post_detail, edit_post, remove_post, up_vote, down_vote, votes, public_post
from notification.views import notifications

urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('follow/<int:author_id>/', follow),
    path('unfollow/<int:author_id>/', unfollow),
    path('notifications/', notifications),
    path('postform/', post_form_view),
    path('post/<int:post_id>/edit/', edit_post),
    path('post/<int:post_id>/remove/', remove_post),
    path('upvote/<int:post_id>/', up_vote),
    path('downvote/<int:post_id>/', down_vote),
    path('votes/', votes),
    path('post/<int:post_id>/public/', public_post, name="public_post"),
    path('post/<int:post_id>/', post_detail, name="post"),
    path('admin/', admin.site.urls),
    path('list/', author_list),
    path('find/', find_list),
    path('<str:username>/edit/', edit_author),
    path('<str:username>/remove/', remove_author),
    path('<str:username>/public/', author_view, name="public"),
    path('<str:username>/', author, name="author"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

