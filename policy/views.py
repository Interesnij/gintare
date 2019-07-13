from django.views.generic.base import TemplateView
from generic.controllers import PageNumberView
from generic.mixins import CategoryListMixin

class PolicyView(PageNumberView,TemplateView,CategoryListMixin):
	template_name="policy.html"
