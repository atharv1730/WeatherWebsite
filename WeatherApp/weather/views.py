from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=911f5b7fb5715798f68e0b7ed2c31b23'
  return render(request, 'weather/index.html')
