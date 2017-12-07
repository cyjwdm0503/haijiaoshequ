# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from collections import OrderedDict


def index(request, name):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.



def main(request, room_id, name):
    context = OrderedDict({'id': room_id,
               'base': {'info': '来自于十里彩云间，理工学子大家都懂的', 'money': "1230.0",'square':"09",'floor': '9', 'totalfloor': '21'},
               'type': {"hezu": 1, "zhengzu": 0, "duwei": 1, "yangtai": 1, "piaochuang": 1, "liangren": 1,
                        "kongtiao": 1, "nansheng": 0,
                        "nvsheng": 1, "yi": 1, "er": 0, "san": 0, "si": 0, "liji": 1, "yizhou": 0, "yiyue":0 },
               'img': {'src':'/static/phone/全部合租/房间8.jpg','alt':'房间8'}});
    return JsonResponse(context, json_dumps_params={'sort_keys': True})
