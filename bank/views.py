from django.shortcuts import render, redirect, render_to_response
from .forms import CommentForm
from .models import Semester, Branch, Subject, College, Comments


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
        'SELECT * FROM bank_subject WHERE college_id=%s AND branch_id = %s AND semester_id = %s',
        [cid, bid, sid])
    return render(request, 'bank/subjects.html', {'subject_views': subject_views, 'cid': cid, 'bid': bid, 'sid': sid})

# 'SELECT * FROM bank_subject WHERE branch_id = %(key)s AND semester_id = %(key)s', [param, params2]


def show_sem(request, cid, bbid):
    semester_views = Semester.objects.all()
    return render(request, 'bank/semester.html', {'semester_views': semester_views, 'bbid': bbid, 'cid': cid})


def show_paper(request, subid):
    comments = Comments.objects.raw('SELECT * FROM bank_Comments WHERE subject_id = %s', [subid])
    question_views = Subject.objects.get(id=subid)
    jayeshform = CommentForm
    return render(request,'bank/question_paper.html',{'question_views': question_views, 'comments': comments, 'subid': subid,
                                                      'jayeshform': jayeshform})


def comments(request, subid):
    comments = Comments.objects.raw('SELECT * FROM bank_Comments WHERE subject_id = %s', [subid])
    question_views = Subject.objects.get(id=subid)
    jayeshform = CommentForm
    if request.POST:
        jayeshform = CommentForm(request.POST)
        if jayeshform.is_valid():
            jayeshform.save()

            return render(request, 'bank/question_paper.html',
                          {'question_views': question_views, 'comments': comments, 'subid': subid,
                           'jayeshform': jayeshform})

    else:
        jayeshform = CommentForm()

        return render(request, 'bank/question_paper.html',
                      {'question_views': question_views, 'comments': comments, 'subid': subid,
                       'jayeshform': jayeshform, })
