from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostFeaturedView,
    BlogPostCategoryView,
    BlogPostCategoryFeaturedView,
)

urlpatterns = [
    path("", BlogPostListView.as_view()),
    path("featured", BlogPostFeaturedView.as_view()),
    path("<category>/featured", BlogPostCategoryFeaturedView.as_view()),
    path("category", BlogPostCategoryView.as_view()),
    path("<slug>", BlogPostDetailView.as_view()),
]
