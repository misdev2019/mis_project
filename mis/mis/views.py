from django.shortcuts import render
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.models import User
from app1.utils.email_send import send_register_email, send_reset_password_email
from app1.models import *

def index(request):
	return render(request,'login.html',{})

def login(request):

	username = request.POST.get("username",None)
	password = request.POST.get("password",None)
	# user = User.objects.create_user(username = '12', email = "123@123.com", password = password)	
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			auth.login(request,user)
			return JsonResponse({
				'status' : 'success',
				'code' : '200',
				'message' : '登录成功',
				'username' : username,
				'password' : password,
			
			})
	else:
		return JsonResponse({
			'status' : 'error',
			'code' : '400',
			'message' : '账号或密码错误',
			'username' : username,
			'password' : password,
		})

def homepage(request):
	return render(request,'index.html',{})


def signup(request):
	# register_form = RegisterForm(request.POST)
	# if register_form.is_valid():
		username = request.POST.get("username", None)
		if(User.objects.filter(username=username)):
			return JsonResponse({
				'status' : 'error',
				'code' : '400',
				'message' : '账号已被注册',
				'username' : username,
			})
		password = request.POST.get("password", None)
		email = request.POST.get("email", None)
		if(User.objects.filter(email=email)):
			return JsonResponse({
				'status' : 'error',
				'code' : '400',
				'message' : '邮箱已被注册',
				'username' : username,
				'password' : password,
				'email' : email,
			})
		user = User.objects.create_user(username = username, password = password, email = email)
		user.is_active = False # 设置为未激活状态
		user.save()
		send_register_email(email, "register") # 调用发送邮件
		return JsonResponse({
			'status' : 'success',
			'code' : '200',
			'message' : '请查收邮件激活账号',
			'username' : username,
			'password' : password,
			'email' : email,
		})
	
def active(request, active_code):
	# 如果保存的随机码中有刚才生成的那个，就说明成功验证
	all_records = EmailVerifyRecord.objects.filter(code = active_code)
	if all_records:
		for record in all_records:
			email = record.email
			user = User.objects.get(email = email)
			user.is_active = True
			user.save()
	else:
		return render(request, "login.html")
	return render(request, "login.html")

def reset_password(request):
	# register_form = RegisterForm(request.POST)
	# if register_form.is_valid():
		username = request.POST.get("username", None)
		new_password = request.POST.get("password", None)
		email = request.POST.get("email", None)
		users = User.objects.filter(email=email, username=username)
		if users :
			for user in users:
				user.set_password(new_password)
				user.is_active = False # 设置为未激活状态
				user.save()
				send_reset_password_email(email, "reset_password") # 调用发送邮件
			return JsonResponse({
				'status' : 'success',
				'code' : '200',
				'message' : '账号已冻结，请查收邮件确认重置密码',
				'username' : username,
				# 'password' : new_password,
				'email' : email,
			})
		else:
			return JsonResponse({
				'status' : 'error',
				'code' : '400',
				'message' : '用户不存在，请重新输入',
				'username' : username,
				# 'password' : new_password,
				'email' : email,
			})

def confirm_reset(request, active_code):
	all_records = EmailVerifyRecord.objects.filter(code = active_code)
	if all_records:
		for record in all_records:
			user = User.objects.get(email=record.email)
			user.is_active = True
		context = {
			'status' : 'success',
			'code' : '200',
			'message' : '密码已重置，请重新登录',
		}
	else:
		context = {
			'status' : 'error',		
			'code' : '400',
			'message' : '信息有误，请重新找回密码',
		}
	return render(request, 'login.html', context)

