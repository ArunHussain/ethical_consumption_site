from django.urls import path
from django.conf.urls import handler404
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('energy/', views.energy, name='energy'),
    path('tech/', views.tech, name='tech'),
    path('food_drink/', views.food_drink, name='food_drink'),
    path('fashion/', views.fashion, name='fashion'),
    path('preferences/', views.survey, name='survey'),
    path('error/', views.error, name='error'),
    path('company/<str:company_name>', views.company_page, name='company_page')
    
]
