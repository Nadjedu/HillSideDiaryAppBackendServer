from rest_framework import permissions


class CanActionUser(permissions.BasePermission):
    message = "User does not have permission to retrieve User data."

    def has_object_permission(self, request, view, obj):
        return obj == request.user
