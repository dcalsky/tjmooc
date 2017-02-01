from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def show(request):
    return render(request, 'user.show.html')


def new(request):
    return render(request, 'user.new.html')


@require_POST
def create(request):
    """
    Handle post request
    return Json
    """
    return JsonResponse()