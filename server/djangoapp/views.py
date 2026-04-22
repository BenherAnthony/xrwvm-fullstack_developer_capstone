from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .models import CarMake, CarModel
from .populate import initiate

logger = logging.getLogger(__name__)


# LOGIN
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "status": "Failed"})


# LOGOUT
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})


# REGISTER (IMPORTANT — DO NOT REMOVE)
@csrf_exempt
def registration(request):
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    if User.objects.filter(username=username).exists():
        return JsonResponse({"userName": username, "error": "Already Registered"})

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email
    )

    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


# ✅ GET CARS (NEW)
def get_cars(request):
    try:
        if CarMake.objects.count() == 0:
            initiate()

        car_models = CarModel.objects.select_related('car_make')

        cars = []
        for car_model in car_models:
            cars.append({
                "CarModel": car_model.name,
                "CarMake": car_model.car_make.name
            })

        return JsonResponse({"CarModels": cars})

    except Exception as e:
        return JsonResponse({"error": str(e)})