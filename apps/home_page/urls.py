from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('<slug:uri>/', home_page, name='home'),
]