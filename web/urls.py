from django.urls import path
from  . import views

urlpatterns =[
    path('',views.index,name='index'),
    # path('<int:id>',views.get_name,name='get_name')
    path('test/',views.test)

]