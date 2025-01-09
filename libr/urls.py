from django.urls import path, include
from rest_framework import routers

from libr.apps import LibrConfig
from libr.views import AuthorViewSet, BookViewSet, ReadingViewSet

app_name = LibrConfig.name

router_habit = routers.DefaultRouter()
router_habit.register(r'authors', AuthorViewSet, basename='author')
router_habit.register(r'books', BookViewSet, basename='book')
router_habit.register(r'readings', ReadingViewSet, basename='reading')

urlpatterns = [
    path('', include(router_habit.urls)),
]
