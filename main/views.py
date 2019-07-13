from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from news.models import New
from movies.models import Movie
from generic.controllers import PageNumberView
from django.conf import settings
from guestbook.models import Guestbook
from django.http import HttpResponse,HttpResponseRedirect
from gintare.forms import FeedbackForm
from django.core.mail import send_mail, BadHeaderError


class MainPageView(PageNumberView,TemplateView,CategoryListMixin):
	template_name="main/mainpage.html"
	news=New.objects.all()[0:10]
	movie1=Movie.objects.filter(category__order=1)[0:3]
	movie2=Movie.objects.filter(category__order=2)[0:3]
	movie3=Movie.objects.filter(category__order=3)[0:3]
	movie4=Movie.objects.filter(category__order=4)[0:3]
	movie5=Movie.objects.filter(category__order=5)[0:3]
	movie6=Movie.objects.filter(category__order=6)[0:3]
	movie7=Movie.objects.filter(category__order=7)[0:3]
	movie8=Movie.objects.filter(category__order=8)[0:3]
	movie9=Movie.objects.filter(category__order=9)[0:3]
	movie10=Movie.objects.filter(category__order=10)[0:3]
	movie11=Movie.objects.filter(category__order=11)[0:3]
	movie12=Movie.objects.filter(category__order=12)[0:3]
	movie13=Movie.objects.filter(category__order=13)[0:3]
	movie14=Movie.objects.filter(category__order=14)[0:3]
	movie15=Movie.objects.filter(category__order=15)[0:3]

	def get_context_data(self,**kwargs):
		context=super(MainPageView,self).get_context_data(**kwargs)
		context["news"]=self.news
		context["movie1"]=self.movie1
		context["movie2"]=self.movie2
		context["movie3"]=self.movie3
		context["movie4"]=self.movie4
		context["movie5"]=self.movie5
		context["movie6"]=self.movie6
		context["movie7"]=self.movie7
		context["movie8"]=self.movie8
		context["movie9"]=self.movie9
		context["movie10"]=self.movie10
		context["movie11"]=self.movie11
		context["movie12"]=self.movie12
		context["movie13"]=self.movie13
		context["movie14"]=self.movie14
		context["movie15"]=self.movie15
		return context

def FeedbackView(request):

    if request.method == 'POST':
        form1 = FeedbackForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            email = form1.cleaned_data['email']
            message = form1.cleaned_data['message']
            recipients = ['ochkarik1983@mail.ru', 'dvizhenietv@gmail.com']
            try:
                send_mail('На сайте "" оставили сообщение', 'Написал {}, почта {}, сообщение "{}"'.format(name, email, message), settings.EMAIL_HOST_USER, recipients)
                send_mail('Спасибо за сообщение на сайте ...', 'Дорогой {}, Спасибо, что оставили сообщение на сайте ... Мы рады любому отзыву или обращению!'.format(name), settings.EMAIL_HOST_USER, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse ('!')
    else:
        form1 = FeedbackForm()
    return HttpResponse ('!')
