"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include
import account.views

urlpatterns = [  #앞에는 어떤주소로 오면 동작시킬거고 뒤에은 어떤 뷰를 동작시킬거야 라고 설정, .as_view()는 앞의(RequestListView)클래스뷰를 함수형 뷰로 바꿔주는 효과가 있어서 써준다. name=은 해당 url패턴의 이름이라고 보면된다.
    path('request/', include('request.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('',  LoginView.as_view(template_name='account/login.html'), name='login'),
]
