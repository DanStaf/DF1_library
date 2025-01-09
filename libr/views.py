from django.shortcuts import render
from rest_framework import viewsets, filters

from libr.models import Author, Book, Reading
from libr.serializers import AuthorSerializer, BookSerializer, ReadingSerializer
from users.permissions import IsManagerClass
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    filterset_fields = "__all__"
    # /books/?title=text
    # /books/?title=&authors=1&year=&genre=
    # /books/?year=1998

    search_fields = ['title', 'authors__first_name', 'authors__last_name']
    # ?search=text

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
