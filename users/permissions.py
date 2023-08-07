from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return bool(request.user == obj and request.user.is_authenticated)


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsAccountOwnerOrAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return bool(
            (request.user == obj or request.user and request.user.is_admin)
            and request.user.is_authenticated
        )
