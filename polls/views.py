from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('heloowl..s.dfsdf')
def test(request, id):
    return HttpResponse('test222 %d' %id)
def hello(request,id):
    return HttpResponse('hello %d' %id)