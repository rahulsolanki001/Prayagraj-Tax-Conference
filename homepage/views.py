from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
# Create your views here.

def homepage_view(request):
	form=Registerform(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			instance=form.save(commit=False)
			#name=form.cleaned_data('name')
			#profession=form.cleaned_data('profession')
			#arrival_date=form.cleaned_data('arrival_date')
			instance.save()
			messages.success(request,'You have been registered sucessfully !!')
			return redirect('/homepage')

	return render (request,'homepage/register.html',{'form':form})