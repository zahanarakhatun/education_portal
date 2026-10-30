from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('courses/<slug:course_slug>/learn/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('courses/<slug:slug>/enroll/', views.enroll_course, name='enroll_course'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/course/create/', views.create_course, name='create_course'),
    path('teacher/course/<slug:slug>/edit/', views.edit_course, name='edit_course'),
    path('teacher/course/<slug:slug>/add-lesson/', views.add_lesson, name='add_lesson'),
]