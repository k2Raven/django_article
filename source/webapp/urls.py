from django.urls import path
from webapp.views import IndexView, article_create_view, article_view, article_update_view, article_delete_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/add/', article_create_view, name='article_create'),
    path('article/<int:pk>/', article_view, name='article_view'),
    path('article/<int:pk>/update/', article_update_view, name='article_update_view'),
    path('article/<int:pk>/delete/', article_delete_view, name='article_delete_view')
]