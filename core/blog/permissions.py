from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermission(BasePermission):
    
    def has_permission(self, request, view):
        # Everyone can read
        if request.method in SAFE_METHODS:
            return True
        
        
        # Only logged-in users can create/update/delete
        return request.user and request.user.is_authenticated
    
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user 
        
        # Admin has no restrictions
        if user.role == 'admin':
            True
            
        # Author permission to only their post
        if user.role == 'author':
            return obj.owner == user
        
        
        # Readers can't modify anything
        return False