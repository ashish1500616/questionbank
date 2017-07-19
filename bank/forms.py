from django.contrib.auth.models import User
from django import forms
from .models import Comment,Reject


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Reject
        fields = '__all__'


