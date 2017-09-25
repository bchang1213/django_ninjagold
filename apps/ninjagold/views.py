# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, 'ninjagold/index.html')

def process(request):
	return redirect('/')