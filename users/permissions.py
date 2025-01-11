from rest_framework.permissions import BasePermission


class IsManagerClass(BasePermission):

    message = 'Only manager have access to this action'

    def has_permission(self, request, view):
        return request.user.is_manager
