from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Application

from .forms import ApplicationForm
# Create your views here.

def home(request):
    return render(request, "home.html")

def add(request):
    if  request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            emloyee_item = form.save(commit=False)
            emloyee_item.save()
            return redirect('/')
    else:
        form = ApplicationForm()
    return render(request, "apply.html", {'form':form})

def list(request):
    queryset = Application.objects.all()
    List = {
        'object_list':queryset
    }
    return render(request, "list.html", List)