from django.urls import path
from . import views
import re
from app import models
urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.user,name='user'),
    path('dele/<int:id>/',views.dele,name='dele'),
    path('weblog/<username>',views.weblog,name='weblog')
]