from rest_framework.permissions import BasePermission


class IsStaffUser(BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False

        return request.user.is_staff
