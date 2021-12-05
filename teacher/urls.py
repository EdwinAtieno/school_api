from django.urls import path
from teacher import views

urlpatterns = [
    path('', views.user_list),
    path('user/<int:pk>/', views.user_detail),
]