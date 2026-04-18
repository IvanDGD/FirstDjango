from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    path('management/', views.management),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('branches/', views.branches),
    path('branches/<str:city>/', views.branch_detail),
]