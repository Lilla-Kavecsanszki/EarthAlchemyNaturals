from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_vip_box,
         name='create_vip_box'),
]
