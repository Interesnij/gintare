from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic.dates import ArchiveIndexView
from .models import AMovie, AComment
from django.views.generic.detail import DetailView
from generic.mixins import PageNumberMixin
from django.views.generic.base import ContextMixin
from generic.controllers import PageNumberView
from a_category.models import ACategory
from django.http import HttpResponse
import json
from django.views import View
from django.contrib.contenttypes.models import ContentType
from main.models import LikeDislike
from main.forms import CommentForm
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.contrib import auth
from django.shortcuts import render_to_response, get_object_or_404, redirect


class AMovieListView(PageNumberView,ArchiveIndexView,CategoryListMixin):
	model=AMovie
	date_field="posted"
	template_name="a_movies_index.html"
	paginate_by=20
	allow_empty=True
	allow_future=True
	make_object_list=True
	tag=""

	def get(self,request,*args,**kwargs):
		if self.kwargs["pk"] == None:
			self.cat=ACategory.objects.first()
		else:
			self.cat=ACategory.objects.get(pk=self.kwargs["pk"])
		return super(AMovieListView,self).get(request,*args,**kwargs)

	def get_queryset(self):
		movie=AMovie.objects.filter(category=self.cat)
		if self.tag:
			movie=AMovie.objects.all()
			movie=movie.filter(tags__name=self.tag)
		return movie

	def get_context_data(self,**kwargs):
		context=super(AMovieListView,self).get_context_data(**kwargs)
		context["category"]=self.cat
		context["tag"]=self.tag
		return context


class AMovieDetailView(PageNumberView,DetailView,PageNumberMixin):
	model=AMovie
	template_name="a_movies.html"
	movies=AMovie.objects.all()[0:3]
	popular=AMovie.objects.order_by("-views")[0:3]
	comment_form = CommentForm
	success_url="/"

	def get(self,request,*args,**kwargs):
		movie = AMovie.objects.get(pk=self.kwargs["pk"])
		self.comments = movie.acomment_set.all().order_by('path')
		if "movie" not in request.COOKIES:
			movie = AMovie.objects.get(pk=self.kwargs["pk"])
			movie.views += 1
			movie.save()

		return super(AMovieDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AMovieDetailView,self).get_context_data(**kwargs)
		context["movies"]=self.movies
		context["popular"]=self.popular
		context["comments"]=self.comments
		context['form'] = self.comment_form
		return context


@require_http_methods(["POST"])
def a_add_comment(request, a_id):

    form = CommentForm(request.POST)
    article = get_object_or_404(AMovie, id=a_id)

    if form.is_valid():
        comment = AComment()
        comment.path = []
        comment.article_id = article
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()
        try:
            comment.path.extend(AComment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)
        comment.save()
    return HttpResponse("!")

class ALastCommentView(TemplateView,CategoryListMixin):
	template_name="a_last_comment.html"

	def get_context_data(self,**kwargs):
		context=super(ALastCommentView,self).get_context_data(**kwargs)
		last_comment=AComment.objects.last()

		context["last_comment"]=last_comment
		return context
