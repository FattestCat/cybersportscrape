from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=now)
    tags = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # pylint: disable=no-member
        super().save(*args, **kwargs)
        for word in self.content.lower().split():
            try:
                wd = morph.parse(word)[0].normal_form
                word_in_db = Word.objects.get(word=wd)
                word_in_db.count = word_in_db.count + 1
                word_in_db.save(update_fields=['count'])
            except ObjectDoesNotExist:
                wd = morph.parse(word)[0].normal_form
                w = Word(word=wd, count=1)
                w.save()


class Tag(models.Model):
    tag = models.CharField(max_length=200)


class Word(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, blank=True)
