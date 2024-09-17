from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class Listtodo(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class Detailtodo(generics.RetrieveUpdateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class Createtodo(generics.CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class Deletetodo(generics.DestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer