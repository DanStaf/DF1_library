from django.shortcuts import render
from rest_framework import viewsets

from libr.models import Author, Book, Reading
from libr.serializers import AuthorSerializer, BookSerializer, ReadingSerializer
from users.permissions import IsManagerClass


# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsManagerClass]

        return super().get_permissions()


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsManagerClass]

        return super().get_permissions()


class ReadingViewSet(viewsets.ModelViewSet):

    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def get_permissions(self):
        self.permission_classes = [IsManagerClass]
        return super().get_permissions()
