from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from twitteruser.views import index, Author, follow, unfollow, edit_author, remove_author, author_list, find_list, AuthorView 
from authentication.views import signup_view, logout_view, login_view
from tweet.views import index, edit_post, remove_post, up_vote, down_vote, post_form_view, PostDetail, PublicPost 
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
    path('altpost/<int:post_id>/public/', PublicPost.as_view(), name="public_post"),
    path('altpost/<int:post_id>/', PostDetail.as_view()),
    path('admin/', admin.site.urls),
    path('list/', author_list),
    path('find/', find_list),
    path('<str:username>/edit/', edit_author),
    path('<str:username>/remove/', remove_author),
    path('<str:username>/public/', AuthorView.as_view(), name="public"),
    path('<str:username>/', Author.as_view(), name="author"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

