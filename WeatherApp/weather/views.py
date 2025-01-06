from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=27101254d3f497eed5b1d80a07b3fcd1'
  return render(request, 'weather/index.html')
