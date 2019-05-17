from django.shortcuts import render
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.models import User

def index(request):
	return render(request,'login.html',{})

def login(request):

	username = request.POST.get("username",None)
	password = request.POST.get("password",None)	
	user = auth.authenticate(username=username,password=password)
	if user is None:
		return JsonResponse({
			'status' : 'error',
			'code' : '400',
			'message' : '账号或密码错误'
		})
	else:
		auth.login(request,user)
	return JsonResponse({
		'status' : 'success',
		'code' : '200',
		'message' : '登录成功'
	})

def homepage(request):
	return render(request,'index.html',{})