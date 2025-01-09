from rest_framework import routers
from rest_framework.permissions import AllowAny

from users.views import UserViewSet, email_verification
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = UsersConfig.name

router_user = routers.DefaultRouter()
router_user.register("", UserViewSet, basename='user')

urlpatterns = [

    path('login/',
         TokenObtainPairView.as_view(
             permission_classes=(AllowAny,)
         ),
         name='login'),
    path('token/refresh/',
         TokenRefreshView.as_view(
             permission_classes=(AllowAny,)
         ),
         name='token_refresh'),

    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),

]

urlpatterns += router_user.urls
