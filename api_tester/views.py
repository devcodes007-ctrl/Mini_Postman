from django.http import JsonResponse


def home(request):
    data = {
        "message": "Welcome to Mini Postman!",
        "status": "success",
        "project": "Mini Postman API Tester"
    }

    return JsonResponse(data)