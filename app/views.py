from django.shortcuts import render

from django.http import HttpResponse
from app import models as appModel

# Create your views here.

def index(request):
    return  HttpResponse('app test')

def user(request):
    if request.method == 'GET':
        user_list =appModel.user.objects.all()
        return render(request,"app/index.html",{"user_list":user_list})
        # return HttpResponse('get')
    elif request.method =='POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        tel = request.POST.get('tel')
        email =request.POST.get('email')
        appModel.user.objects.create(account=user,password=pwd,tel=tel,email=email)
        user_list = appModel.user.objects.all()
        return render(request,"app/index.html" ,{"user_list":user_list})
        # return HttpResponse('注册成功!')
def dele(request,id):
    if request.method =='GET':
        # uid = request.GET.get(id)
        return HttpResponse(id)


def weblog(request,username):
    return HttpResponse(username)