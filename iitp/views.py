from django.views import generic
from django.http import HttpResponse
import datetime
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Iitppaper

# Create your views here.


class Frontpage(generic.ListView):
    template_name = 'bank/front.html'

    def get_queryset(self):
        return Iitppaper.objects.all()


class Streampage(generic.ListView):
    template_name = 'bank/stream.html'

    def get_queryset(self):
        return Iitppaper.objects.all()