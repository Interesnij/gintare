from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from dvig.forms import FeedbackForm

class ContactView(TemplateView,CategoryListMixin):
    template_name = 'contacts.html'

def FeedbackView(request):

    if request.method == 'POST':
        form1 = FeedbackForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            email = form1.cleaned_data['email']
            message = form1.cleaned_data['message']
            recipients = ['vestatrade21@mail.ru']
            try:
                send_mail('На сайте "vesta-t.ru" оставили сообщение', 'Написал "{}", почта "{}", сообщение "{}"'.format(name, email, message), settings.EMAIL_HOST_USER, recipients)
                send_mail('Спасибо за сообщение на сайте vesta-t.ru', 'Дорогой {}, Спасибо, что оставили сообщение на сайте vesta-t.ru. Мы торгуем трикотажем оптом и в розницу, и рады любому отзыву или обращению!'.format(name), settings.EMAIL_HOST_USER, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse ('!')
    else:
        form1 = FeedbackForm()
    return HttpResponse ('!')
