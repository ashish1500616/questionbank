from django.views import generic
from django.http import HttpResponse
import datetime
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import  Semester, Branch, Subject ,College


def indexPage(request):
    college_views=College.objects.all()
    return render(request,'bank/indexpage.html',{'college_views':college_views})



def show_branch(request,pk):
    branch_views = Branch.objects.all()
    return render(request, 'bank/branch.html', {'branch_views': branch_views,'pk':pk})


def show_subject(request,cid,bid,sid):
    # query = 'SELECT * FROM bank_subject WHERE branch_id = %s AND semester_id = %s', % [param, params2]
    subject_views = Subject.objects.raw('SELECT * FROM bank_subject WHERE college_id=%s AND branch_id = %s AND semester_id = %s', [cid,bid, sid])
    return render(request, 'bank/subjects.html', {'subject_views': subject_views})

# 'SELECT * FROM bank_subject WHERE branch_id = %(key)s AND semester_id = %(key)s', [param, params2]


def show_sem(request,cid,bbid):
    semester_views = Semester.objects.all()
    return render(request, 'bank/semester.html', {'semester_views': semester_views,'bbid':bbid,'cid':cid})
