from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def create(request):
    """Handle Login Post Request"""

    return JsonResponse({})
