from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.
def frontpage(request):
    city = request.GET.get('City')
    url = "http://api.weatherapi.com/v1/current.json?key=3db1f7bb90624f7c80f143933201612&q=" + str(city)
    try:
        response = requests.get(url)
        temp = response.json()['current']['temp_c']
        city = response.json()['location']['name']
        country = response.json()['location']['country']
    except KeyError:
        city = None
        temp = None
        country = None
    return render(request, 'front/index.html', {'temp': temp, 'city': city, 'country': country})
