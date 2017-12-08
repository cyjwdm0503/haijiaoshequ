# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'base/(?P<room_id>[0-9]+)/(?P<microseconds>[0-9]+)', views.main, {'name':'房间基础信息'}),
    url(r'search/',views.search,{'name':'异步查询房间信息'}),
    url(r'^', views.index, {'name': '海骄社区'})
]