from django.urls import path

from . import views

urlpatterns = [
    #127.0.0.0:8000/polls
    path('', views.index,name='index'),
    #127.0.0.1/polls/1
    path('<int:id>/', views.test,name='test'),
    #127.0.0.1/polls/1/hello
    # path('<int:id>/hello/',views.hello,name='hello')
    path('hello/<int:id>/', views.hello, name='hello')

]