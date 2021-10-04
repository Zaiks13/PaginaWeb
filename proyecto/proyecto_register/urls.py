from django.urls import path
from . import views

urlpatterns = [
    path('', views.csv_form),
    path('list/', views.csv_list)
]