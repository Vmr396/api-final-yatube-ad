from rest_framework import viewsets, filters, permissions
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment, Follow
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from api.permissions import IsAuthorOrReadOnly


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if self.request.user == serializer.validated_data['following']:
            raise ValidationError('Нельзя подписаться на самого себя')
        serializer.save(user=self.request.user)
