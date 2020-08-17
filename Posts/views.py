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

    def create(self, request, *args, **kwargs):
        author_id = Token.objects.get(key=self.request.auth.key).user_id
        serializer = self.serializer_class(data=request.data, context={'author_id': author_id})
        if serializer.is_valid():
            models.Post.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Post was not created'
        }, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     author_id = Token.objects.get(key=self.request.auth.key).user_id
    #     serializer.save(User=author_id, status=Post.SENT)