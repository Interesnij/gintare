from django.conf.urls import url
from .views import ProfileUserView


urlpatterns = [
    url(r'^(?P<username>[\w\-]+)/$', ProfileUserView.as_view(), name='profile-user'),
]
