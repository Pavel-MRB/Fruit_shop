from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.item2_index, name='item2_index'),
    path('<int:pk>/', views.item2_detail,name='item2_detail'),
    path('about_us/',views.about_us, name='about_us')
]