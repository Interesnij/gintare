from django import forms

from movies.models import Comment


class CommentForm(forms.Form):

    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    comment_area = forms.CharField(
        label="",widget=forms.Textarea(
                attrs={'class': 'input-md round form-control', 'placeholder': 'Напишите что-нибудь','rows':'8','cols':'0','style':'height: 84px;'}
            )
    )
