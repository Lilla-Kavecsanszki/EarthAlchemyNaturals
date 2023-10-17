from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership_view, name='app_membership_view'),
    path('create-vip-box/', views.create_vip_box,
         name='create_vip_box'),
    path('delete-vip-box/', views.delete_vip_box, name='delete_vip_box'),
]
