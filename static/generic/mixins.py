from django.views.generic.base import ContextMixin
from articles.models import Articles

class CategoryListMixin(ContextMixin):

	def get(self,request,*args,**kwargs):

		return super(CategoryListMixin,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"]=self.request.path
		context["articles"]=Articles.objects.all()[0:8]
		return context

class PageNumberMixin(CategoryListMixin):
	def get_context_data(self,**kwargs):
		context=super(PageNumberMixin,self).get_context_data(**kwargs)
		try:
			context["pn"]=self.request.GET["page"]
		except KeyError:
			context["pn"]="1"
		return context
