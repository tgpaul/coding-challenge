from django.db import models

# Create your models here.
class Country(models.Model):
    country_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)

class City(models.Model):
    city_code = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    city_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    locality_verbose = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    cuisines = models.CharField(max_length=255)
    average_cost_for_two = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    has_table_booking = models.CharField(max_length=255)
    has_online_delivery = models.CharField(max_length=255)
    is_delivering_now = models.CharField(max_length=255)
    switch_to_order_menu = models.CharField(max_length=255)
    price_range = models.CharField(max_length=255)
    aggregate_rating = models.CharField(max_length=255)
    rating_color = models.CharField(max_length=255)
    rating_text = models.CharField(max_length=255)
    votes = models.CharField(max_length=255)

class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_country_name = models.CharField(max_length=255)
    user_city_name = models.CharField(max_length=255)
    user_country_code = models.CharField(max_length=255)
    user_city_code = models.CharField(max_length=255)