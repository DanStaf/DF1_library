from rest_framework import routers
from rest_framework.permissions import AllowAny

#from users.views import UserViewSet
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = UsersConfig.name

urlpatterns = [

]
