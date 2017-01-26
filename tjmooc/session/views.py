from django.shortcuts import render
from django.http import JsonResponse


def new(request):
    """Render Login Page"""
    return render(request, 'session.new.html')


def create(request):
    """Handle Login Post Request"""
    return JsonResponse({})
