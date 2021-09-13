from rest_framework import permissions


class CanRetrieveUser(permissions.BasePermission):
    message = "User does not have permission to retrieve User data."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
