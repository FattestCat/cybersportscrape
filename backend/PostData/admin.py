from django.contrib import admin
from .models import Post, Word, Tag

admin.site.register(Post)
admin.site.register(Word)
admin.site.register(Tag)

# Register your models here.
