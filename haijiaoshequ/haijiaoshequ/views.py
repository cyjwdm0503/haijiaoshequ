# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request,name='haijiaoshequ'):
    template =  loader.get_template('index.html');
    context = {'name':name}
    return HttpResponse(template.render(context, request))


def search(request,name='haijiaoshequ'):
    template =  loader.get_template('search.html');
    context = {'name':name}
    return HttpResponse(template.render(context, request))
# Create your views here.


def apply(request,name='haijiaoshequ'):
    template =  loader.get_template('apply.html');
    context = {'name':name}
    return HttpResponse(template.render(context, request))



def phone_index(request,name='haijiaoshequ'):
    template =  loader.get_template('phone_index.html');
    context = {'name':name}
    return HttpResponse(template.render(context, request))