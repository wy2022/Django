from Django.urls import path
from . import views



urlpatterns = [
    path('index/<str:account>/<str:password>/<str:hycard>/',views.index,name='index'),
]