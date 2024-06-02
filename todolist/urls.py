
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index')
    #Send to the index function of the views file
]