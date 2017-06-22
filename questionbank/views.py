from __future__ import unicode_literals

from django.shortcuts import render

def homePage(request):
	return render(request,'bank/front.html',{})