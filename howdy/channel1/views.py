from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import status as http_status
from rest_framework.response import Response
from .serializer import *
from django.contrib.auth.models import User





class CreateUser(APIView):

    def post(self, request):

        data=request.data
        id = request.user
        print(">>>>>>>>>>",id)
        user=User.objects.get(id=id)
        print("????????????????????",user)
        serializer = ContactSerializer(data=data,instance=user)
        if serializer.is_valid():
            voyage=serializer.save()
            data_change = {"change":"created","model":"Voyage"}
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

# Create your views here.
