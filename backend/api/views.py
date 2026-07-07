from django.shortcuts import render
from django.http import JsonResponse

def weather(request):
    return JsonResponse({
        "city": "Copenhagen",
        "temperature": 18,
    })
