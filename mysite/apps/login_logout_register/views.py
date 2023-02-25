from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from dashboard.models import UserInfo
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'client/index.html')
        else:
            return render(request, 'login_logout_register/login.html')
    @csrf_exempt
    def post(self, request):
        data = {}
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        

        if not UserInfo.objects.filter(username=username).exists():
            data['error'] = '该账户不存在，请注册'
            # print(data)
            return JsonResponse(data)
        user = authenticate(request, username=username, password=password)
        if not user:
            data['error'] = '密码错误请重新输入'
            # print(data)
            return JsonResponse(data)
        else:
            login(request, user)
            # print(data)
        return JsonResponse(data)


class Logout(View):

    def get(self, request):

        logout(request)
        return render(request, 'login_logout_register/login.html')


class Register(View):

    def get(self, request):
        return render(request, 'login_logout_register/register.html')
    @csrf_exempt
    def post(self, request):
        
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        
        data = {}
        if UserInfo.objects.filter(username=username).exists():
            
            data['error'] = '该用户已存在，重新创建账户'
            # print(data)
            return JsonResponse(data)
        user = UserInfo.objects.create(username=username, password=password) 
        user.password = make_password(password)  # 明文密码经过加密处理
        user.save()
        
        data['error'] = ''       
        return JsonResponse(data)

