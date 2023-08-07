from django.shortcuts import render

# Create your views here.
# identification/views.py
from django.shortcuts import render, redirect
from .models import User

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        birth_date = request.POST['birth_date']
        User.objects.create(name=name, birth_date=birth_date)
        return redirect('user_list')

    return render(request, 'add_user.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
