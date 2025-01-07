from django.shortcuts import render
import requests

def index(request):
    # OpenWeatherMap API URL
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d18fc568438a833cbcd4fdeb36def429"   # I deactivated this API Key. You will have to create your own and use it.

    city = "Las Vegas"  # Default city
    city_weather = {}  # Initialize city_weather dictionary

    if request.method == "POST":
        city = request.POST.get("city", "Las Vegas")  # Get city from user input

    try:
        # Make API request
        r = requests.get(url.format(city))
        r.raise_for_status()  # Raise HTTPError for bad responses
        data = r.json()

        # Extract weather details
        city_weather = {
            "city": city,
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon'],
        }
    except:
        city_weather = {"error": "Unable to retrieve data. Please enter a valid city."}

    # Render template with weather data
    return render(request, 'weather/index.html', {"city_weather": city_weather})
