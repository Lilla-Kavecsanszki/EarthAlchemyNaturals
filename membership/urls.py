from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_vip_box,
         name='create_vip_box'),
    path('membership/', views.membership_view, name='app_membership_view')
]
