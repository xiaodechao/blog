from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from dashboard.models import UserInfo
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_exempt



# class Register(View):

#     def get(self, request):
#         pass

#     def post(self, request):
#         pass

class Index(View):

    def get(self, request):
        return render(request, 'client/index.html')

    # def post(self, request):
    #     pass
