from django.shortcuts import render, redirect
from admind.models import Employee
from .forms import *

def index(request):

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def display_emp(request):
    items = Employee.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'home.html', context)

def display_card(request):
    items = Employee.objects.all()
    

    context = {
        'items' : items
        
    }

    return render(request, 'home.html', context)

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
        return render(request,'add_new.html',{'form':form})