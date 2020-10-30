from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    ]