from django import forms
from guestbook.models import Guestbook

class GuestbookForm(forms.ModelForm):
	class Meta:
		model=Guestbook
		exclude=['user', ] 
