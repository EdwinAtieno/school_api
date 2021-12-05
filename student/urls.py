from django.urls import path
from student import views

urlpatterns = [
    path('', views.student_list),
    path('user/<int:pk>/', views.student_detail),
]