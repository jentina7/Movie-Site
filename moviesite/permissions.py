from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == "pro":
            return True
        if request.user.status == "simple" and obj.movie_status == "simple":
            return True

        return False




