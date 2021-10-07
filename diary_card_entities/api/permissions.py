from rest_framework import permissions


class CanActionTarget(permissions.BasePermission):
    message = "User does not have permission to action target."

    def has_object_permission(self, request, view, obj):
        return obj.patient_uuid == request.user


class CanRetrieveEmotion(permissions.BasePermission):
    message = "User does not have permission to retrieve emotion."

    def has_object_permission(self, request, view, obj):
        return obj.patient_uuid == request.user


class CanActionDiaryEntity(permissions.BasePermission):
    message = "User does not have permission to action diary entity."

    def has_object_permission(self, request, view, obj):
        return obj.patient_uuid == request.user

