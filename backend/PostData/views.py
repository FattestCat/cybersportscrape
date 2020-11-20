from django.shortcuts import render

from rest_framework import viewsets

from .models import Post, Word
from.serializers import PostSerializer, WordSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer