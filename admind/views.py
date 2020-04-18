from django.shortcuts import render
from admind.models import Employee

def index(request):

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def display_emp(request):
    items = Employee.objects.all()

    context = {
        'items' : items
    }

    return render(request, 'index.html', context)