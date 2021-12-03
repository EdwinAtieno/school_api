from django.urls import path
from staff import views

urlpatterns = [
    path('', views.user_list),
    path('user/<int:pk>/', views.user_detail),
]