from django.shortcuts import render
from django.http import JsonResponse
import requests



def get_coordinates(city):
    api_url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        api_url,
        params={
            "name": city,
            "count": 1,
        },
    )

    print(response.json())


def weather(request):

    city = "Copenhagen"
    get_coordinates(city)


    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    #print(response.json())

    return JsonResponse(response.json())
