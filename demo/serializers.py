from rest_framework import serializers
from .models import Survivors,Reports,Locations

class LocationsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Locations
    fields = ['latitude','longitude']


class SurvivorsSerializer(serializers.ModelSerializer):
  # ser = serializers.RelatedField(source='location',read_only=True)
  location = LocationsSerializer(many=True)
  class Meta:
    model = Survivors
    fields = ['name','age','gender','location']

class ReportsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reports
    fields = ['infected','non_infected']

# class LocationsSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Locations
#     fields = ['latitude','longitude']
