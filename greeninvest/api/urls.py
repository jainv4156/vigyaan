from django.urls import path
from . import views 

urlpatterns = [
    path('getcatagories/', views.getcatagories, name='getcatagories'),
    path('getenvirementalist/', views.getenvirementalist, name='getenvirementalist')

]