from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.home, name='customer'),
    path('courier/', views.home, name='courier'),
]
