# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random

def index(request):
	try:
		request.session['gold_amount']
	except KeyError:
		request.session['gold_amount'] = 0

	try:
		request.session['activitylist']
	except KeyError:
		request.session['activitylist'] = []

	return render(request, 'ninjagold/index.html')

def process(request, building_type):
	if building_type == "farm":
		earnedgold = random.randint(10,21)
		request.session['gold_amount'] += earnedgold
		message = "Earned "+str(earnedgold)+" gold from the farm!"
		request.session['activitylist'].insert(0,message)

	elif building_type == "cave":
		earnedgold = random.randint(5,11)
		request.session['gold_amount'] += earnedgold
		message = "Earned "+str(earnedgold)+" gold from the cave!"
		request.session['activitylist'].insert(0,message)

	elif building_type == "house":
		earnedgold = random.randint(2,6)
		request.session['gold_amount'] += earnedgold
		message = "Earned "+str(earnedgold)+" gold from the house!"
		request.session['activitylist'].insert(0,message)

	elif building_type == "casino":
		earnedgold = random.randint(0,51)
		request.session['gold_amount'] += earnedgold
		message = "Earned "+str(earnedgold)+" gold from the casino!"
		request.session['activitylist'].insert(0,message)
	return redirect('/')