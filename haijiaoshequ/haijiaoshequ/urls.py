# -*- coding: utf-8 -*-
"""haijiaoshequ URL Configuration

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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
import  views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^zhanshi/',include('room.urls')),
    url(r'^search',views.search,{'name':'我要租房'}),
    url(r'^apply',views.apply,{'name':'房东加盟'}),
    url(r'^phone',views.phone_index,{'name':'手机版海骄社区'}),
    url(r'^menu/(?P<city>.+)',views.menu,{'name':'所有地理信息与位置'}),
    url(r'^room',include('room.urls')),
    url(r'^',views.index,{'name':'海骄社区'})
]
