from django.shortcuts import render

from rest_framework import viewsets

from .models import Post, Word, CleanWord
from .serializers import PostSerializer, WordSerializer, CleanWordSerializer

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

