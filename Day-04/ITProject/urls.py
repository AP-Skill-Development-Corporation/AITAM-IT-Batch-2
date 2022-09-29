"""ITProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ITApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('w/',views.demo),
    path('p/<str:n>/',views.gy),
    path('k/<str:en>/<int:g>/',views.et),
    path('y/<str:z>/',views.dy),
    path('j/',views.dm),
    path('v/',views.gv),
    path('b/<str:w>/',views.dfa),
    path('ph/',views.rg),
    
]
