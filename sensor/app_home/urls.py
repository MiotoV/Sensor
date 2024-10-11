from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_list/', views.data_list, name='data_list'),
]
