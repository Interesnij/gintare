from django.conf.urls import url
from .views import ProfileUserView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ProfileUserView.as_view(), name='profile-user'),
]
