from django.shortcuts import render

from rest_framework import viewsets

from .models import Post, Word
from .serializers import PostSerializer, WordSerializer

class PostViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class WordViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = Word.objects.all()
    serializer_class = WordSerializer
