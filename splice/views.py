from django.shortcuts import render, redirect
from django.http import HttpResponse

# rest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
from .forms import RegistrationForm1, RegistrationForm2
from .models import vendor, bidder

def home(request):
    return render(request, 'index.html', {})

def contact(request):
    print("Jay")
    return render(request, 'contact.html', {})

@api_view(['POST'])
def registration(request):
    userType = request.headers.get('type')
    email = request.data['email_conf']
    if userType=='bidder':
        form = RegistrationForm1(request.data)
        email_found = bidder.objects.filter(email=email)
    else:
        form = RegistrationForm2(request.data)
        email_found = vendor.objects.filter(email=email)
    if email_found.count()>0:
        return HttpResponse("Email already exists")
    if form.is_valid():
        # form.save()
        return HttpResponse("User Successfully registred!")
    else:
        return Response(form.errors, status= HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        if bidder.objects.filter(email=email, password=password).exists():
            name = bidder.objects.filter(email=email).values('firstName').first()
            name = name['firstName']
            return render(request, 'bidder.html', {'name':name})
        elif vendor.objects.filter(email=email, password=password).exists():
            name = vendor.objects.filter(email=email).values('firstName').first()
            name =  name['firstName']
            return render(request, 'vendor.html', {'name':name})
        else:
            return Response("Something went Wrong", status=HTTP_400_BAD_REQUEST)
    except Exception as exe:
        return Response(str(exe), status=HTTP_400_BAD_REQUEST)