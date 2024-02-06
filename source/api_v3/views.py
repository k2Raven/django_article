from django.db.models import Count
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api_v3.serializers import ArticleModelSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from webapp.models import Article


class ArticleModelVIewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method == 'GET':
        # if self.action in ('list', 'retrieve', 'get_comments_count', 'get_article_comments_count'):
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated()]

    # def list(self, request, *args, **kwargs):
    #     return Response({'test': 'test1'})

    @action(methods=["GET"], detail=False, url_path="comments-count")
    def get_comments_count(self, request, *args, **kwargs):
        return Response(self.queryset.aggregate(count=Count('comments')))

    @action(methods=["GET"], detail=True, url_path="comments-count")
    def get_article_comments_count(self, request, pk, *args, **kwargs):
        article = self.get_object()
        return Response({"count": article.comments.count()})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
