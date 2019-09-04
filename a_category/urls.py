from django.contrib.auth.decorators import permission_required
from a_category.views import ACategoriesEdit
from django.conf.urls import url

urlpatterns=[
	url(r'^$', ACategoriesEdit.as_view(), name="a_categories_edit"),
]
