from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailView, GenericAPIView

urlpatterns = [
    path('articles/', article_list),
    path('article/<int:pk>', article_detail),
    path('articleapi/', ArticleAPIView.as_view()),
    path('articleapi/<int:id>', ArticleDetailView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view())
]