from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Survivors,Reports,Locations
from .serializers import SurvivorsSerializer,ReportsSerializer,LocationsSerializer
from rest_framework import status


@api_view(['GET','POST','PUT'])
def survivors_api(request, pk=None):
  if request.method == 'GET':
    id = pk
    if id is not None:
      suv = Survivors.objects.get(id=id)
      serializer = SurvivorsSerializer(suv)
      return Response(serializer.data)
    suv = Survivors.objects.all()
    serializer = SurvivorsSerializer(suv, many=True)
    return Response(serializer.data)

  if request.method == 'POST':
    serializer = SurvivorsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'PUT':
    id = pk
    suv = Survivors.objects.get(pk=id)
    serializer = SurvivorsSerializer(suv, data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Updated'})
    return Response(serializer.errors)

@api_view(['GET'])
def reports_api(request, pk=None):
  if request.method == 'GET':
    id = pk
    if id is not None:
      rep = Reports.objects.get(id=id)
      serializer = ReportsSerializer(rep)
      return Response(serializer.data)
    rep = Reports.objects.all()
    serializer = ReportsSerializer(rep, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def locations_api(request, pk=None):
  if request.method == 'PUT':
    id = pk
    loc = Locations.objects.get(pk=id)
    serializer = LocationsSerializer(loc, data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Updated'})
    return Response(serializer.errors)