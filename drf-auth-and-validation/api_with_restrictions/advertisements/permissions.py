from rest_framework import permissions


class EditPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff is True:
            return True
        return obj.creator == request.user
