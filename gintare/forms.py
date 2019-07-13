from main.models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    name = forms.CharField( label="",widget=forms.TextInput(
            attrs={'class': 'input-md round form-control ', 'placeholder': ' Ваше имя'}
        ))
    email = forms.EmailField( label="",widget=forms.EmailInput(
            attrs={'class': 'input-md round form-control', 'placeholder': 'Ваша почта'}
        ))
    message = forms.CharField( label="",widget=forms.Textarea(
            attrs={'class': 'input-md round form-control', 'placeholder': 'Ваше сообщение','rows':'0','cols':'0','style':'height: 84px;'}
        ))
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
