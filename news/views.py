from generic.mixins import CategoryListMixin
from django.views.generic.dates import ArchiveIndexView
from news.models import New
from django.views.generic.detail import DetailView
from generic.mixins import PageNumberMixin
from django.shortcuts import redirect
from django.shortcuts import render
from generic.controllers import PageNumberView
from django.db.models import Q

class NewsListView(PageNumberView,ArchiveIndexView,CategoryListMixin):
    model=New
    date_field="posted"
    template_name="news_index.html"
    paginate_by=10
    allow_empty=True
    allow_future=True
    news=New.objects.all()[0:6]
    def get_queryset(self):
        new=super(NewsListView,self).get_queryset()
        if self.search:
            new=new.filter(Q(title__icontains=self.search)|Q(description__icontains=self.search))
        return new

    def get_context_data(self,**kwargs):
        context=super(NewsListView,self).get_context_data(**kwargs)
        context["news"]=self.news
        return context

class NewDetailView(DetailView,PageNumberMixin,CategoryListMixin):
    model=New
    template_name="new.html"
    news=New.objects.all()[0:6]
    def get(self,request,*args,**kwargs):
        new = New.objects.get(pk=self.kwargs["pk"])
        new.views += 1
        new.save()
        return super(NewDetailView,self).get(request,*args,**kwargs)
    try:
        if new_id in request.COOKIES:
            redirect('news_detail', pk=new_id)

        else:
            new = New.objects.get(id=new_id)
            new.views += 1
            new.save()
            response = redirect('news_detail', pk=new_id)
            response.set_cookie(new_id, "test")
    except:
        pass

    def get_context_data(self,**kwargs):
        context=super(NewDetailView,self).get_context_data(**kwargs)
        context["news"]=self.news
        return context
