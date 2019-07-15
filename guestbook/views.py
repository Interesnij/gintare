from django.http import HttpResponse
from django.views.generic.dates import ArchiveIndexView
from guestbook.models import Guestbook
from guestbook.forms import GuestbookForm
from generic.mixins import CategoryListMixin
from django.conf import settings
from django.core.mail import send_mail

class GuestbookView(ArchiveIndexView,CategoryListMixin):
	model=Guestbook
	date_field="posted"
	template_name="guestbook.html"
	paginate_by=1
	allow_empty=True
	form=None
	def get(self,request,*args,**kwargs):
		self.form=GuestbookForm(initial={"user":request.user})

		return super(GuestbookView,self).get(request,*args,**kwargs)
	def get_context_data(self,**kwargs):
		context=super(GuestbookView,self).get_context_data(**kwargs)
		context["form"]=self.form
		return context
	def post(self,request,*args,**kwargs):
		self.form=GuestbookForm(request.POST)
		if self.form.is_valid():
			guest=self.form.save(commit=False)
			guest.user=request.user
			guest=self.form.save()

			if request.is_ajax() :
				return HttpResponse ('!')
			return super(GuestbookView,self).get(request,*args,**kwargs)
		return super(GuestbookView,self).get(request,*args,**kwargs)

class GuestView(ArchiveIndexView,CategoryListMixin):
	template_name="guest_list.html"
	paginate_by=20
	date_field="posted"
	allow_empty=True
	model=Guestbook
