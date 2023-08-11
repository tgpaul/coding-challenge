from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import City, Country, Restaurant, User
from .forms import CollectUser

def homePage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def citiesPage(request):
  cities = City.objects.all().values()
  template = loader.get_template('cities.html')
  context = {
    'cities' : cities,
  }
  return HttpResponse(template.render(context, request))

def displayAllRestaurants(request):
  restaurants = Restaurant.objects.all().values()
  template = loader.get_template('restaurants.html')
  context = {
    'restaurants' : restaurants,
  }
  return HttpResponse(template.render(context, request))
  
def collectPage(request):
  if request.method == 'POST':
    form = CollectUser(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/restaurantlist')
  else:
      form = CollectUser()

  return render(request, 'collectpage.html',{'form':form})

def restaurantList(request):

  user = User.objects.last()
  country = user.user_country_name
  city = user.user_city_name
  valid_country = Country.objects.filter(country_name = country).values()
  valid_city = City.objects.filter(city_name = city).values()

  # print("USER")
  # print(user.user_country_name)
  print("CITIES")
  print(valid_city)
  print("COUNTRY")
  print(valid_country)
  
  context = {
    'country': valid_country,
    'city': valid_city
  }


  template = loader.get_template('restaurantlist.html')
  return HttpResponse(template.render(context, request))    

