from rest_framework.permissions import BasePermission


class IsLoggedUser(BasePermission):
    """
    Only exposes the endpoint for the logged user
    """

    def has_object_permission(self, request, view, obj):

        return request.user == obj
