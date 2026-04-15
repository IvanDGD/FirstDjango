from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiplication_table, name='get_request')
]