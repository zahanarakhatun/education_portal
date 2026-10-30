from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

# 1. Home Page
def home(request):
    courses = Course.objects.filter(is_published=True)[:6]
    return render(request, 'home.html', {'courses': courses})

# 2. All Courses
def course_list(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'courses/list.html', {'courses': courses})

# 3. Single Course Detail
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.all()
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

# 4. Lesson Detail
@login_required
def lesson_detail(request, course_slug, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson.html', {'lesson': lesson})

# 5. Enroll
@login_required
def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('my_courses')

# 6. My Courses
@login_required
def my_courses(request):
    enrolls = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrolls': enrolls})

# 7. Teacher Dashboard
@login_required
def teacher_dashboard(request):
    my_courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/dashboard.html', {'my_courses': my_courses})

def create_course(request):
    return render(request, 'teacher/create.html')

def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'teacher/edit.html', {'course': course})

def add_lesson(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'teacher/add_lesson.html', {'course': course})

# 8. Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f"'{username}' এই নামটি আগেই নেয়া হয়েছে।")
            return render(request, 'register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "এই Email আগেই ব্যবহার করা হয়েছে।")
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        auth_login(request, user)
        return redirect('home')
        
    return render(request, 'register.html')

# 9. Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username বা Password ভুল!")
            return render(request, 'login.html')
            
    return render(request, 'login.html')

# 10. Logout
def logout_view(request):
    logout(request)
    messages.success(request, "আপনি Logout হয়ে গেছেন।")
    return redirect('home')