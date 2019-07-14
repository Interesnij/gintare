from main.models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    name = forms.CharField( label="",widget=forms.TextInput(
            attrs={'class': 'form-control dvt-shadow-2 dvt-shadow-focus-4 dvt-transition m-b-2', 'placeholder': ' Ваше имя'}
        ))
    email = forms.EmailField( label="",widget=forms.EmailInput(
            attrs={'class': 'form-control dvt-shadow-2 dvt-shadow-focus-4 dvt-transition m-b-2', 'placeholder': 'Ваша почта'}
        ))
    message = forms.CharField( label="",widget=forms.Textarea(
            attrs={'class': 'form-control dvt-shadow-2 dvt-shadow-focus-4 dvt-transition m-b-2', 'rows':'8', 'placeholder': 'Ваше сообщение','rows':'0','cols':'0','style':'height: 84px;'}
        ))
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
