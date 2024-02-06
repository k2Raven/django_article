from django.urls import path, include
from rest_framework import routers
from api_v3.views import ArticleModelVIewSet, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v3'

router = routers.DefaultRouter()
router.register(r'articles', ArticleModelVIewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
