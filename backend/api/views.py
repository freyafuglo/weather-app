from django.shortcuts import render
from django.http import JsonResponse
import requests



def get_coordinates(city):
    #uses the api from open meto that translates city names to
    api_url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        api_url,
        params={
            "name": city,
            "count": 1,
        },
    )

    data = response.json()

    result = data["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]

    return latitude, longitude

def get_weather(latitude, longitude):
    api_url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        api_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
            "timezone": "auto",
        },
    )

    return response.json()


def weather(request):

    city = request.GET.get("city")
    lat, lon = get_coordinates(city)

    weather_data = get_weather(lat, lon)

    print(weather_data)


    return JsonResponse({
    "city": city,
    "temperature": weather_data["current"]["temperature_2m"],
    "wind_speed": weather_data["current"]["wind_speed_10m"],
    "time": weather_data["current"]["time"],
})
