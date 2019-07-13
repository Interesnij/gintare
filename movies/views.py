from generic.mixins import CategoryListMixin
from django.views.generic.dates import ArchiveIndexView
from movies.models import Movie, Comment
from django.views.generic.detail import DetailView
from generic.mixins import PageNumberMixin
from django.views.generic.base import ContextMixin
from generic.controllers import PageNumberView
from category.models import Category
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
from django.views.generic.base import TemplateView


class MovieListView(PageNumberView,ArchiveIndexView,CategoryListMixin):
	model=Movie
	date_field="posted"
	template_name="movies_index.html"
	paginate_by=20
	allow_empty=True
	allow_future=True
	make_object_list=True
	tag=""

	def get(self,request,*args,**kwargs):
		if self.kwargs["pk"] == None:
			self.cat=Category.objects.first()
		else:
			self.cat=Category.objects.get(pk=self.kwargs["pk"])
		return super(MovieListView,self).get(request,*args,**kwargs)

	def get_queryset(self):
		movie=Movie.objects.filter(category=self.cat)
		if self.tag:
			movie=Movie.objects.all()
			movie=movie.filter(tags__name=self.tag)
		return movie

	def get_context_data(self,**kwargs):
		context=super(MovieListView,self).get_context_data(**kwargs)
		context["category"]=self.cat
		context["tag"]=self.tag
		return context


class MovieDetailView(PageNumberView,DetailView,PageNumberMixin):
	model=Movie
	template_name="movies.html"
	movies=Movie.objects.all()[0:3]
	popular=Movie.objects.order_by("-views")[0:3]
	comment_form = CommentForm
	success_url="/"

	def get(self,request,*args,**kwargs):
		movie = Movie.objects.get(pk=self.kwargs["pk"])
		self.comments = movie.comment_set.all().order_by('path')
		if "movie" not in request.COOKIES:
			movie = Movie.objects.get(pk=self.kwargs["pk"])
			movie.views += 1
			movie.save()

		return super(MovieDetailView,self).get(request,*args,**kwargs)
	def view(request):
  		response = HttpResponse( 'blah' )
  		response.set_cookie( 'movie', 'movie' )
  		return response

	def get_context_data(self,**kwargs):
		context=super(MovieDetailView,self).get_context_data(**kwargs)
		context["movies"]=self.movies
		context["popular"]=self.popular
		context["comments"]=self.comments
		context['form'] = self.comment_form
		return context


class VotesView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )

def addviews(request, movie_id):
    try:
        if movie_id in request.COOKIES:
            redirect('movies_detail', pk=movie_id)
        else:
            movie = Movie.objects.get(id=movie_id)
            movie.view += 1
            movie.save()
            response = redirect('movies_detail', pk=movie_id)
            response.set_cookie(movie_id, "movie")
            return response
    except :
        pass
    return redirect('movies_detail', pk=movie_id)

@require_http_methods(["POST"])
def add_comment(request, movie_id):

    form = CommentForm(request.POST)
    article = get_object_or_404(Movie, id=movie_id)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.article_id = article
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()
        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)
        comment.save()
    return HttpResponse("!")

class LastCommentView(TemplateView,CategoryListMixin):
	template_name="last_comment.html"

	def get_context_data(self,**kwargs):
		context=super(LastCommentView,self).get_context_data(**kwargs)
		last_comment=Comment.objects.last()

		context["last_comment"]=last_comment
		return context
