from django.urls import path
from django.views.generic import RedirectView
from webapp.views import IndexView, ArticleCreateView, ArticleView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', RedirectView.as_view(pattern_name='index')),
    path('articles/add/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update_view'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete_view')
]