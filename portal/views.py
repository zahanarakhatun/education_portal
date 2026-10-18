from django.shortcuts import render,redirect
from.forms import AdminRegistrationForm
from.models import CustomUserModel
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    course_list = [
        {
            'title': 'Web Development with Django',
            'description': 'Learn HTML, CSS, Bootstrap, and Django to build full-stack web apps.',
            'badge': 'Popular'
        },
        {
            'title': 'Python Programming Basics',
            'description': 'Master core Python programming fundamentals from beginner to advanced level.',
            'badge': 'New'
        },
        {
            'title': 'Frontend Web Design',
            'description': 'Create responsive websites using Bootstrap 5, HTML5, and CSS3.',
            'badge': 'Featured'
        }
    ]
    return render(request, 'courses.html', {'courses': course_list})

def dashboard(request):
    return render(request, 'dashboard.html')

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'Admin'  # <-- Ekhane code diye set, form theke na
            user.save()
            return redirect('login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'register.html', {'form': form})

def admin_login(request):
    # Django er default login view use korte paro, ba custom
    from django.contrib.auth import authenticate, login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')