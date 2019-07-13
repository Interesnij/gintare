from guestbook.views import GuestbookView, GuestView
from django.conf.urls import url

urlpatterns=[
	url(r'^$', GuestbookView.as_view(), name="guestbook"),
	url(r'^list/$', GuestView.as_view(), name="guest_list"),
]
