from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.view_home, name="home"),
    path('vehicles', views.view_vehicles, name="vehicles"),
    path('recycle-view', views.view_recyclebin, name="recycleview"),
    path('contact', views.view_contact, name="contact"),
    path('about', views.view_about, name="about"),
    path('vehicles/addvehicle', views.view_addvehicle, name="addvehicle"),
    path('vehicles/addvehicle/save', views.save_vehicle, name="create_vehicle"),
    path('vehicles/updatevehicle', views.updatevehicle, name="updatevehicle"),
    path('vehicles/voidedvehicle/<uuid:id>', views.voidedvehicle, name="voidedvehicle"),
    path('vehicles/unvoidedvehicle/<uuid:id>', views.unvoidedvehicle, name="unvoidedvehicle"),
    path('vehicles/permanentdeletevehicle/<uuid:id>', views.permanentvehicle, name="permanentvehicle"),
    
]