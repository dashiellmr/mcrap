from django.urls import path
from .views import rap_transform, mcrap


app_name='mcrap'
urlpatterns = [
    path('', mcrap, name='mcrap'),
    path('rap_transform/', rap_transform, name='rap_transform'),
]