from django import forms
from .models import City, Country, Restaurant, User

class CollectUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name','user_country_name','user_city_name']


