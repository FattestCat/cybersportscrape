from rest_framework import serializers
from .models import Post, Word, CleanWord, PostDot, WordDot, CleanWordDot

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content','date','tags']


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'count', 'tags']

class CleanWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanWord
        fields = ['id', 'word', 'count', 'tags']



class PostDotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDot
        fields = ['id','title','content','date','tags']


class WordDotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDot
        fields = ['id', 'word', 'count', 'tags']

class CleanWordDotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordDot
        fields = ['id', 'word', 'count', 'tags']
