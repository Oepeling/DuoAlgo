from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lessons/', views.get_lessons, name='lessons'),
    path('lesson/<int:lesson_id>/', views.get_lesson_info, name='single_lesson'),
]