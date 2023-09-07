from django.urls import path
from . import views

urlpatterns = [
    path('<int:herb_id>/', views.star_ingredient, name='star_ingredient'),
]
