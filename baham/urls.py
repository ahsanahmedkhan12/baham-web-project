from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.view_home, name="home"),
    path('vehicles', views.view_vehicles, name="vehicles"),
    path('contact', views.view_contact, name="contact"),
    path('about', views.view_about, name="about"),
    path('vehicles/addvehicle', views.view_addvehicle, name="addvehicle"),
    path('vehicles/addvehicle/save', views.save_vehicle, name="create_vehicle"),
    path('vehicles/updatevehicle', views.updatevehicle, name="updatevehicle"),
    path('vehicles/deletevehicle', views.deletevehicle, name="deletevehicle"),
    
]