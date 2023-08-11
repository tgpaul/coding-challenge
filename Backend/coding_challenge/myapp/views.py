from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import City, Country, Restaurant

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
  
def collectPage(request):
  if request.method == 'POST':
    data = request.POST['data']
    return redirect('result',data=data)

  template = loader.get_template('collectpage.html')
  return HttpResponse(template.render())

def displayPage(request):
  data = request.GET.get('data')
  return render(request, 'result_template.html', {'data':data})

def displayAllRestaurants(request):
  restaurants = Restaurant.objects.all().values()
  template = loader.get_template('restaurants.html')
  context = {
    'restaurants' : restaurants,
  }
  return HttpResponse(template.render(context, request))