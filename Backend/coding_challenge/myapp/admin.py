from django.contrib import admin

from .models import City, Country, Restaurant, User

# Register your models here.
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Restaurant)
admin.site.register(User)
