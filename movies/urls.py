from django.contrib.auth.decorators import login_required
from movies.views import MovieListView,MovieDetailView,VotesView,LastCommentView
from django.conf.urls import url
from main.models import LikeDislike
from .models import Movie, Comment
from .views import addviews, add_comment


urlpatterns = [

url(r'^(?P<pk>\d+)/$',MovieListView.as_view(), name="movies_index"),
url(r'^(?P<pk>\d+)/detail/$',MovieDetailView.as_view(), name="movies_detail"),
url(r'^like/(?P<pk>\d+)/$',login_required(VotesView.as_view(model=Movie, vote_type=LikeDislike.LIKE)),name='article_like'),
url(r'^dislike/(?P<pk>\d+)/$',login_required(VotesView.as_view(model=Movie, vote_type=LikeDislike.DISLIKE)),name='article_dislike'),
url(r'^comment/(?P<pk>\d+)/like/$',login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),name='comment_like'),
url(r'^comment/(?P<pk>\d+)/dislike/$',login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),name='comment_dislike'),
url(r'^addview/(?P<view_id>[0-9]+)/$', addviews, name='addviews'),
url(r'^comment/(?P<movie_id>[0-9]+)/$', add_comment, name='add_comment'),
url(r'^last_comment/$', LastCommentView.as_view(), name='last_comment'),

]
