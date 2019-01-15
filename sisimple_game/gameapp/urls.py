from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('create_hero/', views.CreateHero.as_view(),name='create hero'),

]
