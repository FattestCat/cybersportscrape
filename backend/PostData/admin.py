from django.contrib import admin
from .models import Post, Word, Tag, CleanWord

admin.site.register(Post)
admin.site.register(Word)
admin.site.register(Tag)
admin.site.register(CleanWord)

