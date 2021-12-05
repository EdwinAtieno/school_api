from django.urls import path
from student import views

urlpatterns = [
    path('', views.student_list),
    path('teacher/<int:pk>/', views.student_detail),
]