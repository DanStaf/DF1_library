from rest_framework.permissions import BasePermission


class IsManagerClass(BasePermission):

    message = 'Only manager have access to this action'

    def has_object_permission(self, request, view, obj):
        return request.user.is_manager
