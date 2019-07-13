from django.conf.urls import url
from main.views import MainPageView
from . import views

urlpatterns = [
	url(r'^$', MainPageView.as_view(), name="main"),
	url(r'^form', views.FeedbackView, name='FeedbackView'),
]
