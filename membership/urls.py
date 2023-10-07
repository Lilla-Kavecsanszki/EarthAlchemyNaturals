from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create-vip-box/', views.create_vip_box,
         name='create_vip_box'),
    path('', views.membership_view, name='app_membership_view')
]
