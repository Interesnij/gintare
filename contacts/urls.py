from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ContactView.as_view(), name='contacts'),
    url(r'^form', views.FeedbackView, name='FeedbackView'),
]
