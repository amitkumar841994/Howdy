from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import *




class CreateUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data=request.data
        id = request.user.id
        print(">>>>>>>>>>>>>>>>>>",id)
        print(">>>>>>>>>>",id)
        user=UserProfile.objects.get(user=id)
        print("????????????????????",user.mobile)
        data['user_id']=user.id
        print("data>>>>>>>>>",data)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            voyage=serializer.save()
            return Response(serializer.data, status=http_status.HTTP_201_CREATED)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

# Create your views here.
