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

def dm(request):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Sample Page</body></html>")

def gv(request):
	return render(request,'demo.html')

def dfa(request,w):
	return render(request,'html/sample.html',{'g':w})

def rg(r):
	if r.method == "POST":
		a = r.POST['un']
		b = r.POST['pd']
		c = r.POST['em']
		d = r.POST['ea']
		return render(r,'html/display.html',{'ena':a,'ema':c,'eaa':d})	
	return render(r,'html/register.html')
