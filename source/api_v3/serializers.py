from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from webapp.models import Article, Tag


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class ArticleModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        print(instance)
        data = super().to_representation(instance)
        print(data)
        data['author'] = AuthorModelSerializer(instance.author).data
        data['tags'] = TagsModelSerializer(instance.tags.all(), many=True).data
        return data

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'tags', 'comments', 'created_at', 'updated_at']
        read_only_fields = ['comments', 'author']

    def validate_title(self, title):
        if len(title) < 10:
            raise ValidationError("Title must be at least 8 characters")
        return title

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
