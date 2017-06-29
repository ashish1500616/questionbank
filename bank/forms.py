from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from bank.models import Comments


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'body' ]


jayeshform = CommentForm()
