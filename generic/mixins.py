from django.views.generic.base import ContextMixin
from django.conf import settings
from category.models import Category
from taggit.models import Tag
from news.models import New
from movies.models import Movie


class CategoryListMixin(ContextMixin):
	tags=Tag.objects.all()
	last_news=New.objects.all()[0:3]
	last_movie=Movie.objects.all()[0:3]

	def get_context_data(self,**kwargs):
		context=super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"]=self.request.path
		context["tags"]=self.tags
		context["last_news"]=self.last_news
		context["last_movie"]=self.last_movie
		context["categories"]=Category.objects.all()
		return context

class PageNumberMixin(CategoryListMixin):
	def get_context_data(self,**kwargs):
		context=super(PageNumberMixin,self).get_context_data(**kwargs)
		try:
			context["pn"]=self.request.GET["page"]
		except KeyError:
			context["pn"]="1"
		return context
