from rest_framework import serializers
from posts.models import Post, Group, Comment, Follow  # noqa
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого пользователя'
            )
        ]

    def validate_following(self, value):
        if self.context['request'].user == value:
                        raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value
