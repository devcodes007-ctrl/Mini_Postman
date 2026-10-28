from django.http import JsonResponse


def home(request):
    data = {
        "message": "Welcome to Mini Postman!",
        "status": "success",
        "project": "Mini Postman API Tester"
    }

    return JsonResponse(data)

def api_info(request):
    data = {
        "name": "Mini Postman",
        "version": "1.0",
        "description": "A simple API testing tool",
    }

    return JsonResponse(data)

def health(request):
    return JsonResponse({
        "status": "healthy",
        "message": "Mini Postman API is running"
    })