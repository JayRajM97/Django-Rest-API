from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to edit their own profile"""
        #
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
