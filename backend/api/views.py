from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        #returns authenticated user

        return Note.objects.filter(author=user)
        #get notes by a specific author

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class DeleteNote(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):#this function makes sure to let users delete notes that were created by themselves only
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    #get all users

    serializer_class = UserSerializer
    #what kind of data we need to accept from serializer to create new user

    permission_classes = [AllowAny]
    #allow any user, even unauthenticated

