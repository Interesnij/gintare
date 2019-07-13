from django.contrib.auth.decorators import permission_required,login_required
from .views import NewDetailView,NewsListView
from django.conf.urls import url


urlpatterns = [

	url(r'^$', NewsListView.as_view(), name="news_index"),
	url(r'^(?P<pk>\d+)/$', NewDetailView.as_view(), name="news_detail"),
]
