
from django.urls import path
from . views import *
urlpatterns = [
    path('',index,name='index'),
    path('map/', map_view, name='map-view'),
    
]