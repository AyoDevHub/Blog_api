from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermission(BasePermission):
    
    def has_permission(self, request, view):
        # Everyone can read
        if request.method in SAFE_METHODS:
            return True
        
        
        # block unauthenticated user 
        if not request.user or not request.user.is_authenticated:
            return False
            
        
        # Admin always allowed 
        if request.user.role == 'admin':
            return True
        
        
        # Author always allowed
        if request.user.role == 'author':
            return True
        
        
        # Restricting readers from creating
        if request.user.role == 'reader':
            return False
        
        
        return False
            
        
       
    
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user 
        
        # Admin has no restrictions
        if user.role == 'admin':
            return True
            
            
        # Author permission to only their post
        if user.role == 'author':
            return obj.owner == user
        
        
        # Readers can't modify anything
        return request.method in SAFE_METHODS