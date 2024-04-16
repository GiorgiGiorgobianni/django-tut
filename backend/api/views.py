from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    #get all users

    serializer_class = User
    #what kind of data we need to accept from serializer to create new user

    permission_classes = [AllowAny]
    #allow any user, even unauthenticated

