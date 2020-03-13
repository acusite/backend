from rest_framework import serializers
from .models import Like


class LikesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = [
            'event',
            'liked_by',
        ]

    def create(self, validated_data):
        qs = Like.objects.filter(event__slug=self.context.get('slug'), liked_by=self.context.get('user'))
        if qs.exists():
            qs.first().delete()
            return qs.first()
        return Like.objects.create(event__slug=self.context.get('slug'), liked_by=self.context.get('user'))


class LikesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = [
            'event',
            'liked_by',
        ]
