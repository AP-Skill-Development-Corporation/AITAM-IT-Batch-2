from django.shortcuts import render,redirect
from . forms import UsReg
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages

@login_required
def home(request):
	return render(request,'Demo/home.html')

def about(request):
	return render(request,'Demo/about.html')

def register(request):
	if request.method == "POST":
		e = UsReg(request.POST)
		if e.is_valid():
			e.save()
			messages.success(request,"User Created Successfully")
			return redirect('/login')
	e = UsReg()
	return render(request,'Demo/regis.html',{'r':e})