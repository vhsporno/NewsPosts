from rest_framework.permissions import BasePermission, SAFE_METHODS


class CheckPostOwnerOrAny(BasePermission):
    """
    In first step it check has_permission method. Default IsAuthificated method
    Then if user is authoficated go to has_object_permission
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    For safe methods allow permission for any user
    If method in [POST, PATCH, PUT, DELETE] check if object author == request.user
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
