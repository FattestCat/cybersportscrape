from django.contrib import admin
from .models import Post, Word, Tag, CleanWord, PostDot, WordDot, CleanWordDot

admin.site.register(Post)
admin.site.register(Word)
admin.site.register(CleanWord)
admin.site.register(PostDot)
admin.site.register(WordDot)
admin.site.register(CleanWordDot)
admin.site.register(Tag)

