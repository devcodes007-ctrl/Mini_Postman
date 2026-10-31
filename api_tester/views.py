from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'api_tester/index.html')


def home(request):
    return JsonResponse({
        "message": "Welcome to Mini Postman!",
        "status": "success",
        "project": "Mini Postman API Tester"
    })


def api_info(request):
    return JsonResponse({
        "name": "Mini Postman",
        "version": "1.0",
        "description": "A simple API testing tool",
    })


def health(request):
    return JsonResponse({
        "status": "healthy",
        "message": "Mini Postman API is running"
    })