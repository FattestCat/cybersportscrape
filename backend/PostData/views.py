from django.shortcuts import render

from rest_framework import viewsets

from .models import Post, Word, CleanWord, PostDot, WordDot, CleanWordDot
from .serializers import (
        PostSerializer,
        WordSerializer,
        CleanWordSerializer,
        PostDotSerializer,
        WordDotSerializer,
        CleanWordDotSerializer
        )

class PostViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class WordViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class CleanWordViewSet(viewsets.ModelViewSet):
    queryset = CleanWord.objects.all()
    serializer_class = CleanWordSerializer


class PostDotViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = PostDot.objects.all()
    serializer_class = PostDotSerializer


class WordDotViewSet(viewsets.ModelViewSet):
    #pylint: disable=no-member
    queryset = WordDot.objects.all()
    serializer_class = WordDotSerializer

class CleanWordDotViewSet(viewsets.ModelViewSet):
    queryset = CleanWordDot.objects.all()
    serializer_class = CleanWordDotSerializer

