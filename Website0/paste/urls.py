from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/', views.make),
    path('<str:code>/', views.redirector),
]
