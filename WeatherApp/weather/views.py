from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d18fc568438a833cbcd4fdeb36def429"

    city = "Las Vegas"
    r = requests.get(url.format(city)).json()

    city_weather = {
        "city": city,
        "temperature": r['main']['temp'],
        "description": r['weather'][0]['description'],
        "icon": r['weather'][0]['icon'],
    }


    return render(request, 'weather/index.html')


