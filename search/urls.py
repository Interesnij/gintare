from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'movie-filter/', views.movie_filter, name='movie_filter'),
]
