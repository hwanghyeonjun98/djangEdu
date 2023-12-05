from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(req):
    return HttpResponse('Hello World')


def select(req):
    message = '수 하나를 입력해주세요.'
    return HttpResponse(message)


def result(req):
    message = '결과 입니다.'
    return HttpResponse(message)
