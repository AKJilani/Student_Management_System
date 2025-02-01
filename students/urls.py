from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView,
    StudentDeleteView, StudentDetailView, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student/new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]