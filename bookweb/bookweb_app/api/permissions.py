from rest_framework import permissions

class AdminPerm(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # print(request.user)
            # print(request.user.is_staff)
            return bool(request.user and request.user.is_staff)
    
class UserReviewPerm(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
            return True
        else:
        # Check permissions for write request
            # print(obj)
            # print(obj.review_creator)
            # print(request.user)
            return obj.review_creator == request.user or request.user.is_staff