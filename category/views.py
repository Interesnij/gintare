from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin

class CategoriesEdit(TemplateView,CategoryListMixin):
	template_name="categories_edit.html"
