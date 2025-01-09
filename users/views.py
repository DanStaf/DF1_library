from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer

import secrets
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, LOGIN_REDIRECT_URL
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.set_password(new_user.password)

        new_user.is_active = False
        token = secrets.token_hex(16)
        new_user.token = token

        new_user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'

        send_mail(
            "DF 1 Library - email confirm",
            f"To confirm the email please tap on the link: {url}",
            EMAIL_HOST_USER,
            [new_user.email],
            fail_silently=False,
        )

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse("users:user-list"))
