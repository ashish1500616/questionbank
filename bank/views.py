from django.views import generic
from django.http import HttpResponse
import datetime
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Album, Song, Test, Semester, Branch, Subject


class Frontpage(generic.ListView):
    template_name = 'bank/front.html'

    def get_queryset(self):
        return Album.objects.all()


class IndexView(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='cse_third')


class Index2View(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='cse_fourth')


class EceView(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='ece_third')


class Ece2View(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='ece_fourth')


class MechView(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='mech_third')


class Mech2View(generic.ListView):
    template_name = 'bank/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.filter(concatenate='mech_fourth')


class HomeView(generic.ListView):
    template_name = 'bank/home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class Home2View(generic.ListView):
    model = Album
    template_name = 'bank/home2.html'


class Home3View(generic.ListView):
    model = Album
    template_name = 'bank/home3.html'


class Home1View(generic.ListView):
    model = Album
    template_name = 'bank/home1.html'


class DetailView(generic.DetailView):
    model = Album
    template_name = 'bank/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['subject', 'semester', 'branch', 'concatenate', 'upload_paper', ]


class SongCreate(CreateView):
    model = Song
    fields = ['subject', 'semester', 'year', 'upload_solutions', ]


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('bank:index')


class AlbumUpdate(UpdateView):
    model = Album
    success_url = reverse_lazy('bank:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'bank/album_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def Post(self, request):

        form = self.form_class(request.post)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('bank:index')

        return render(request, self.template_name, {'form': form})


def selectCollege(request):
    answer = request.GET['dropdown']
    if answer == "1":
        return redirect('/some/url/')


def show_branch(request):
    branch_views = Branch.objects.all()
    subject_views = Subject.objects.all()
    semester_views = Semester.objects.all()
    return render(request, 'bank/branch.html', {'branch_views': branch_views, 'subject_views': subject_views, 'semester_views': semester_views})


def show_subject(request,bid,sid):
 #   bid = 1
  #  sid = 2
    # query = 'SELECT * FROM bank_subject WHERE branch_id = %s AND semester_id = %s', % [param, params2]
    subject_views = Subject.objects.raw('SELECT * FROM bank_subject WHERE branch_id = %s AND semester_id = %s', [bid, sid])
    return render(request, 'bank/subjects.html', {'subject_views': subject_views})

# 'SELECT * FROM bank_subject WHERE branch_id = %(key)s AND semester_id = %(key)s', [param, params2]


def show_sem(request,bbid):
    semester_views = Semester.objects.all()
    return render(request, 'bank/semester.html', {'semester_views': semester_views,'bbid':bbid})
