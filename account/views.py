from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from django.views.generic import CreateView #글쓰기뷰
from django.urls import reverse, reverse_lazy
from .form import LoginForm

# Create your views here.
from account.form import LoginForm
from .models import Account


class AccountCreateView(CreateView):
    model = Account    #연결할 db모델명
    form_class = UserCreationForm   #일반적인 게시판 형태가 아니기 때문에 회원가입 특화된 폼을 제공받는다.
    success_url = reverse_lazy('request:list')   #완료 후 이동할 페이지
    template_name = 'account/create.html'   #어떤 템플릿을 사용할지 설정
