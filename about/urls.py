from .views import AboutView
from django.conf.urls import url

urlpatterns=[
	url(r'^$', AboutView.as_view(), name="about"),
]
