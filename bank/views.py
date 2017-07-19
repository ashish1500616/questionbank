from django.views import generic
from django.http import HttpResponse
from bank import forms
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, CommentForm, SubjectForm
from .models import Semester, Branch, Subject, College, Question, Comment, Reject, Paper


def indexPage(request):
    college_views = College.objects.all()
    return render(request, 'bank/indexpage.html', {'college_views': college_views})


def show_branch(request, pk):
    branch_views = Branch.objects.all()
    return render(request, 'bank/branch.html', {'branch_views': branch_views, 'pk': pk})


def show_subject(request, cid, bid, sid):
    # query = 'SELECT * FROM bank_subject WHERE branch_id = %s AND semester_id
    # = %s', % [param, params2]
    subject_views = Subject.objects.raw(
        'SELECT * FROM bank_subject WHERE college_id=%s AND branch_id = %s AND semester_id = %s', [cid, bid, sid])
    return render(request, 'bank/subjects.html', {'subject_views': subject_views, 'cid': cid, 'bid': bid, 'sid': sid})

# 'SELECT * FROM bank_subject WHERE branch_id = %(key)s AND semester_id = %(key)s', [param, params2]


def show_sem(request, cid, bbid):
    semester_views = Semester.objects.all()
    return render(request, 'bank/subjects.html', {'subject_views': subject_views, 'cid': cid, 'bid': bid, 'sid': sid})

# 'SELECT * FROM bank_subject WHERE branch_id = %(key)s AND semester_id = %(key)s', [param, params2]


def show_sem(request, cid, bbid):
    semester_views = Semester.objects.all()
    return render(request, 'bank/semester.html', {'semester_views': semester_views, 'bbid': bbid, 'cid': cid})


def show_paper(request, subid):
    question_views = Question.objects.get(subject_id=subid)
    comments_views = Comment.objects.filter(subject_id=subid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.subject_id = question_views.subject_id
            comment.save()
            return redirect('bank:question_paper', subid=comment.subject_id)
    else:
        form = CommentForm()
    return render(request, 'bank/question_paper.html', {'question_views': question_views, 'form': form, 'comments_views': comments_views})

# Comments related methods


@login_required
def comment_approve(request, subid):
    comment = Comment.objects.get(id=subid)
    comment.approve()
    return redirect('bank:question_paper', subid=comment.subject_id)


@login_required
def comment_remove(request, subid):
    comment = Comment.objects.get(id=subid)
    # savinng post primary key as comment.delete will delte it from the a
    comment_id = comment.subject_id
    comment.delete()
    return redirect('bank:question_paper', subid=comment_id)



def form_name_view(request):
    form = forms.FormName()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName(request.POST)

        # Check to see form is valid
        if form.is_valid():

            # Do something.
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])
    return render(request,'bank/form_page.html',{'form':form})


def users(request):
    form = SubjectForm


    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponse('<h1>your question will be uploaded after verification</h1>')

        else:
            print("ERROR!")

    return render(request,'bank/SubjectForm.html',{'form':form})


class PaperCreate(CreateView):
    model = Paper
    fields = ['college', 'semester', 'branch', 'subject', 'upload',]
