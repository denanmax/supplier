from rest_framework.permissions import BasePermission


class IsActiveStuff(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_active and request.user.is_staff
