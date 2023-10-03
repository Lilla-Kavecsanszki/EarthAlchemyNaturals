from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('membership/', views.create_vip_box,
         name='create_vip_box'),
    path('', views.membership_view, name='app_membership_view')
]
