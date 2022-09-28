from django.contrib import admin
from .models import Survivors,Reports,Locations

# Register your models here.
@admin.register(Survivors)
class Survivors(admin.ModelAdmin):
  list_display = ['name','age','gender']


@admin.register(Reports)
class Reports(admin.ModelAdmin):
  list_display = ['infected','non_infected']


@admin.register(Locations)
class Locations(admin.ModelAdmin):
  list_display = ['latitude','longitude']
