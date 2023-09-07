from django.urls import path
from . import views

urlpatterns = [
    path('herbs/<int:herb_id>/', views.star_ingredient, name='star_ingredient'),
]
