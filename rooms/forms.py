from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere", required=False)
    country = CountryField(default="KR", blank=True).formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(), required=False
    )
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
