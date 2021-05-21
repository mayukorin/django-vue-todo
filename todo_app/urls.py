from django.urls import path, include
from . import views

app_name ='todo'
urlpatterns = [
    path('user/create/', views.UserCreateAPIView.as_view()),
    path('password/update/', views.UserPasswordUpdateAPIView.as_view()),
    path('user/profile/update/', views.UserProfileUpdateAPIView.as_view()),
    path('task/create/', views.TaskCreateAPIView.as_view()),
    path('task/list/', views.TaskListAPIView.as_view()),
    path('task/edit/<int:pk>/', views.TaskEditAPIView.as_view()),
    path('task/update/<int:pk>/', views.TaskUpdateAPIView.as_view()),
]