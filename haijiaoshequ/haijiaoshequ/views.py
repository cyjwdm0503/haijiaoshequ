# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request,name='haijiaoshequ'):
    return HttpResponse("Hello, world. You're at the "+ name +" index.")
# Create your views here.
