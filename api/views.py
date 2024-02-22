from django.shortcuts import render
from django.http import HttpResponse
from . import serializers
from main import models , Staff


from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def staff_create(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    staff = Staff.objects.create_user(
        first_name=first_name, 
        last_name = last_name)
    Staff.objects.create(staff = staff)

    return Response('Created')
