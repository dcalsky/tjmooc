from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


def new(request):
    return render(request, 'user.new.html')


def create(request):
    """
    Handle post request
    return Json
    """
    return JsonResponse({})