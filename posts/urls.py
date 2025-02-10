from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('', student_list, name='student-list'),  # API to get all students
    path('<int:pk>/', student_detail, name='student-detail'),  # API for single student
]
