from .models import New
from django import forms

class New2Form(forms.ModelForm):
	class Meta:
		model = New
		exclude = ['likes', 'views']
