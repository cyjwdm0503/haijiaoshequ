# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse

from collections import OrderedDict


def index(request, name='haijiaoshequ'):
    template = loader.get_template('index.html');
    context = {'name': name}
    return HttpResponse(template.render(context, request))


def search(request, name='haijiaoshequ'):
    template = loader.get_template('search.html');
    context = {'name': name}
    return HttpResponse(template.render(context, request))



def apply(request, name='haijiaoshequ'):
    template = loader.get_template('apply.html');
    context = {'name': name}
    return HttpResponse(template.render(context, request))


def phone_index(request, name='haijiaoshequ'):
    template = loader.get_template('phone_index.html');
    context = {'name': name}
    return HttpResponse(template.render(context, request))


def menu(request, city="成都市", name="菜单"):
    context = OrderedDict()
    if (city == "成都市"):
        context = OrderedDict({'一级菜单': {
            '区域': {'锦江区': '锦江区', '青羊区': '青羊区', '金牛区': '金牛区', '成华区': '成华区', '龙泉驿': '龙泉驿', '温江区': '温江区', '双流县': '双流县',
                   '高新区': '高新区', '高新西区': '高新西区'},
            '地铁': {'1号线': '1号线', '2号线': '2号线', '3号线': '3号线', '4号线': '4号线'}},
                               '二级菜单': {
                                   '锦江区': {'全部': '全部', '川师': '川师', '三圣乡': '三圣乡', '万达': '万达', '琉璃场': '琉璃场', '成仁路': '成仁路',
                                           '九眼桥': '九眼桥', '沙河堡': '沙河堡', '攀成钢': '攀成钢', '静居寺': '静居寺', '内环': '内环'},
                                   '青羊区': {'全部': '全部', '金沙': '金沙', '黄田坝': '黄田坝', '外光华': '外光华', '内光华': '内光华',
                                           '外金沙': '外金沙', '浣花小区': '浣花小区', '府南国际': '府南国际', '内环': '内环'}}})
    elif (city == "上海市"):
        context = OrderedDict({'一级菜单': {
            '区域': {'锦江区': '锦江区', '青羊区': '青羊区', '金牛区': '金牛区', '成华区': '成华区', '龙泉驿': '龙泉驿', '温江区': '温江区', '双流县': '双流县'},
            '地铁': {'1号线': '1号线', '2号线': '2号线', '3号线': '3号线', '4号线': '4号线', '5号线': '5号线'}},
            '二级菜单': {'锦江区': {'全部': '全部', '川师': '川师', '三圣乡': '三圣乡', '万达': '万达', '琉璃场': '琉璃场', '成仁路': '成仁路'},
                     '青羊区': {'全部': '全部', '金沙': '金沙', '黄田坝': '黄田坝', '外光华': '外光华', '内光华': '内光华', '外金沙': '外金沙'}}})
    #return HttpResponse(json.dumps(context,sort_keys=True), content_type = "application/json");
    return JsonResponse(context,json_dumps_params={'sort_keys':True})
