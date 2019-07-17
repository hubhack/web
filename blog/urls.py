"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpRequest, HttpResponse, JsonResponse
import datetime
from django.template.loader import get_template
from django.shortcuts import render

def index(request:HttpResponse):
    """视图函数:请求进来返回响应"""
    my_dict = {
        'a':100,
        'b':0,
        'c':list(range(10,20)),
        'd':'abc', 'date':datetime.datetime.now()
    }

    data = ['{}*{}={}'.format(j, i, j*i) for i in range(1, 10)for j in range(1, 10)]

    context = {'content': 'www.magedu.com', 'my_dict':my_dict, 'data':data}
    return render(request, 'index.html', context)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^users/', include("user.urls"))

]



