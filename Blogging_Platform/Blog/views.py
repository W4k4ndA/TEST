from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .models import Blog
from .serializers import BlogSerializer

from django.db.models import Q


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogSearchView(views.APIView):
    def get(self, request, term):
        blogs = Blog.objects.filter(Q(title__icontains=term) | Q(
            content__icontains=term) | Q(tags__icontains=term))
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
