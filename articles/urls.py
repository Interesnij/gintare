from .views import AMovieListView,AMovieDetailView,ALastCommentView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from movies.views import VotesView
from django.conf.urls import url
from main.models import LikeDislike
from .models import AMovie, AComment
from .views import a_add_comment

urlpatterns=[
    url(r'^(?P<pk>\d+)/$',AMovieListView.as_view(), name="a_movies_index"),
    url(r'^(?P<pk>\d+)/detail/$',AMovieDetailView.as_view(), name="a_detail"),
    url(r'^like/(?P<pk>\d+)/$',login_required(VotesView.as_view(model=AMovie, vote_type=LikeDislike.LIKE)),name='a_article_like'),
    url(r'^dislike/(?P<pk>\d+)/$',login_required(VotesView.as_view(model=AMovie, vote_type=LikeDislike.DISLIKE)),name='a_article_dislike'),
    url(r'^comment/(?P<pk>\d+)/like/$',login_required(VotesView.as_view(model=AComment, vote_type=LikeDislike.LIKE)),name='a_comment_like'),
    url(r'^comment/(?P<pk>\d+)/dislike/$',login_required(VotesView.as_view(model=AComment, vote_type=LikeDislike.DISLIKE)),name='a_comment_dislike'),
    url(r'^comment/(?P<a_id>[0-9]+)/$', a_add_comment, name='a_add_comment'),
    url(r'^last_comment/$', ALastCommentView.as_view(), name='a_last_comment'),
]
