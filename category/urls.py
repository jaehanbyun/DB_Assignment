"""category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.base, name='base'),
    path('create/', views.createTable, name='create'),
    path('insert/', views.insertTable, name='insert'),
    path('display/', views.display, name='display'),
    path('inserteach/', views.inserteach, name='inserteach'),
    path('result1/', views.resultview1, name='result1'),
    path('result2/', views.resultview2, name='result2'),
    path('result3/', views.resultview3, name='result3'),
    path('result4/', views.resultview4, name='result4')
]
