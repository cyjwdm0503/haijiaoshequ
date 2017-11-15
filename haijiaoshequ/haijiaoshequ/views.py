# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request,name='haijiaoshequ'):
    template =  loader.get_template('index.html');
    context = {'name':name}
    return HttpResponse(template.render(context, request))
# Create your views here.
