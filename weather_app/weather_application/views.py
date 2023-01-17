from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'f876a1780712f2134ce17364f4947b00'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    name1 = ''
    all_cities = []
    city_tmp = {}

    form = CityForm(request.POST or None)

    if form.is_valid():
        name1 = form.cleaned_data.get("name")
        print(name1)
        form = CityForm(request.POST)
        if City.objects.filter(name=name1).exists():
            pass
        else:
            form.save()

    form = CityForm

    cities = City.objects.order_by("-id")

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        city_tmp = city_info

        all_cities.append(city_info)

    # if name != '':
    #     all_cities.

    # print(city_tmp)
    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, 'weather_application/index.html', context)
