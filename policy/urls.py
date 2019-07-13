from .views import PolicyView
from django.conf.urls import url

urlpatterns=[
	url(r'^$', PolicyView.as_view(), name="policy"),
]
