from django.contrib.auth.decorators import permission_required
from category.views import CategoriesEdit
from django.conf.urls import url

urlpatterns=[
	url(r'^$', CategoriesEdit.as_view(), name="categories_edit"),
]
