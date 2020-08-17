from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import CheckPostOwnerOrAny
from rest_framework.response import Response

from . import serializers, models


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated, CheckPostOwnerOrAny)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
