#from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it.
    Others can only view it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request method is a safe method (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Otherwise, check if the user is the owner of the object
        return obj.owner == request.user
