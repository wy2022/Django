from django.shortcuts import render
from django.http import HttpResponse
from web import models
# Create your views here.
#创建一个字典
# user_list = [
#     {"user":"jack","pwd":"123"},
#     {"user":"tom","pwd":"acc"},
# ]
def index(request):
    # return HttpResponse('web,,index ,hello')
    #返回html页面
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #添加到数据库
        models.UserInfo.objects.create(user=username,pwd=password,tel='13512345678')
        print(username,password)
        # temp ={"user":username,"pwd":password}
        # user_list.append(temp)
    user_list = models.UserInfo.objects.all()#从数据库中读取

    return render(request,'index.html',{"data":user_list}) #后面字典是html页面用

def get_name(request,id):

    return HttpResponse('get_name %d' %id)

def test(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        models.Userinfo.objects.create(username=username,password=password,user_group_id=1)
        # return HttpResponse('post')
        return HttpResponse('注册成功!')
    elif request.method =='GET':
        # return HttpResponse('get')
        user_list =models.Userinfo.objects.all()
        return render(request,'ceshi.html',{"data":user_list})

