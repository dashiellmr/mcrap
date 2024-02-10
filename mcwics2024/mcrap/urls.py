from django.urls import path
from . import views


app_name='mcrap'
urlpatterns = [
    path('', views.mcrap, name='mcrap'),
    path('convert', views.rapTransform, name='convert')
]