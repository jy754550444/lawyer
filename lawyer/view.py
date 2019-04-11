# coding=utf-8
__author__ = 'yy'
from django.shortcuts import render, render_to_response, HttpResponse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User


#登录页
def list(request):
    return render(request, 'static/login.html')

#登录完成页
def finish(request):
    return render(request, 'static/finish.html')

 #律师所
def userDemo(request):
    desc = User.objects.all()[0].get_profile().description
    return HttpResponse(desc)
