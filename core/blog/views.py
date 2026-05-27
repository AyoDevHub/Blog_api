from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from blog.permissions import PostPermission



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    permission_classes = [PostPermission] 
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
