from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homePage, name='HomePage'),
    path('citiespage/', views.citiesPage, name='CitiesPage'),
    path('collectpage/', views.collectPage, name='CollectPage'),
    path('restaurantspage/', views.displayAllRestaurants, name='RestaurantPage')
]
