from django.urls import path
from . import views
import re
from app import models
app_name='app'
urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.user,name='user'),
    path('dele/<int:id>/',views.dele,name='dele'),
    path('weblog/<str:account>/<str:password>/',views.weblog,name='weblog')
]