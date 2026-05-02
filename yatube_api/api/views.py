from rest_framework import viewsets, permissions, filters
from django.contrib.auth import get_user_model
from posts.models import Follow
from api.serializers import FollowSerializer

User = get_user_model()

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
