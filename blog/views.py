from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from blog.custom_blog_post_serializer import CustomBlogData


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryFeaturedView(ListAPIView):
    def get_queryset(self):
        category = self.kwargs.get("category", None)
        queryset = BlogPost.objects.all().filter(
            category=category, category_featured=True
        )
        return queryset

    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data["category"]
        queryset = BlogPost.objects.order_by("-date_created").filter(
            category__iexact=category
        )
        domain = request.get_host()
        print(domain)
        serializer = CustomBlogData(queryset, many=True)

        return Response(serializer.data)
