from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', Detailtodo.as_view()),
    path('', Listtodo.as_view()),
    path('create', Createtodo.as_view()),
    path('delete/<int:pk>', Deletetodo.as_view())
]