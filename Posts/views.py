from rest_framework import generics, status
from . import serializers, models
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if getattr(self.request.user, 'id') == post.getAuthor():
            self.perform_destroy(post)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('You have no access for this action', status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        