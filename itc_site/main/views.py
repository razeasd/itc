from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request,'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request,'main/about.html')
def contacts(request):
    return render(request,'main/contacts.html')

def docs(request):
    return render(request,'main/docs.html')