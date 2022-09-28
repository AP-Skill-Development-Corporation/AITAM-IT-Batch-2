from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse("Hi, Welcome")

def gy(request,n):
	return HttpResponse(f"Hi, Welcome {n}")

def et(request,en,g):
	return HttpResponse(f"Hi, Welcome {en} and your age is: {g}")

def dy(request,z):
	return HttpResponse(f"<h3>Hi, Welcome <span style='color:red'>{z}</span></h3>")


