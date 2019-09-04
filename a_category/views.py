from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin

class ACategoriesEdit(TemplateView,CategoryListMixin):
	template_name="a_categories_edit.html"
