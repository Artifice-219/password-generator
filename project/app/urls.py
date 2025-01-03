from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('get-password/', views.get_password, name='get_password')
]