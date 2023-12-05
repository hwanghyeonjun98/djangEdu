from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random


# Create your views here.
def index(req):
	# template = loader.get_template('index.html')  # templates를 사용하기 위해 settings.py INSTALLED_APPS APP 디렉토리명 추가
	now = datetime.now()
	context = {
		'cur_date': now
	}
	# return HttpResponse(template.render(context, req))
	return render(req, 'first/index.html', context)  # request, temlate 이름, context


def select(req):
	context = {}
	return render(req, 'first/select.html', context)


def result(req):
	choosen = int(req.GET['num'])

	results = []
	if choosen >= 1 and choosen <= 45:
		results.append(choosen)

	box = []
	for i in range(0, 45):
		if choosen != i + 1:
			box.append(i + 1)

	random.shuffle(box)

	while len(results) < 6:
		results.append(box.pop())

	context = {
		'nums': results
	}
	return render(req, 'first/result.html', context)
