from django.views.generic import TemplateView
from generic.mixins import CategoryListMixin
from django.contrib.auth.models import User
from profiles.models import UserProfile
from datetime import datetime, timedelta
from movies.models import Movie


class ProfileUserView(TemplateView, CategoryListMixin):
    template_name = 'user.html'
    username=None
    user1=None
    profile=None
    online=None

    def get(self,request,*args,**kwargs):
        self.user1 = User.objects.get(pk=self.kwargs["pk"])
        self.profile = UserProfile.objects.get_or_create(user=self.user1)[0]
        aaa = datetime.now()
        onl = self.profile.last_activity + timedelta(minutes=1)
        if aaa < onl:
            self.online = 1
        return super(ProfileUserView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['user1'] = self.user1
        context['profile'] = self.profile
        context['online'] = self.online
        return context
