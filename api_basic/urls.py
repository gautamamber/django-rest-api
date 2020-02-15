from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('articles/', article_list),
    path('article/<int:pk>', article_detail),
    path('articleapi/', ArticleAPIView.as_view()),
    path('articleapi/<int:id>', ArticleDetailView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls))

]