from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import *


def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Todo.objects.create(
                title=request.POST.get('s'),
                time=request.POST.get('sana'),
                description =request.POST.get('b'),
                status=request.POST.get('st'),
                student= Student.objects.get(user= request.user)
            )

            return redirect('/todo/')
        data = {
            'rejalar':Todo.objects.filter(student__user=request.user)
        }

        return render(request,'dedline.html',data)
    else:
        return redirect('/')

def loginView(request):
    if request.method =='POST':
        user = authenticate(username=request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request,user)
        return redirect('/todo/')

    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def delete(request,num):
    p = Todo.objects.get(id=num)
    if request.user == p.student.user:
        p.delete()
    return redirect('/todo/')


def signup(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        Student.objects.create(
            fullname = request.POST.get('fl'),
            guruh = request.POST.get('g'),
            st_id = request.POST.get('st'),
            tel = request.POST.get('t'),
            user = u
        )
        return redirect('/')
    return render(request,'register.html')



