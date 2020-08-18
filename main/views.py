from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create.html')


def detail(request):
    return render(request, 'detail.html')