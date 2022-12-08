from django.urls import path
from . import views

urlpatterns = [
   path('', views.hola, name='hola'),
   path('Vader/', views.vader, name='vader'),




]