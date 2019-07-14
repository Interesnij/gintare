from django import forms
from guestbook.models import Guestbook

class GuestbookForm(forms.ModelForm):
	content = forms.CharField(
        label="",widget=forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Напишите что-нибудь','rows':'8','cols':'0','style':'height: 84px;'}
            )
    )
	class Meta:
		model=Guestbook
		exclude=['user', ]
