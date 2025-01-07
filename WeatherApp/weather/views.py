from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=d18fc568438a833cbcd4fdeb36def429"

    city = "Las Vegas"

    r = requests.get(url.format(city))

    print(r.text)

    return render(request, 'weather/index.html')


