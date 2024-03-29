from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist

import pymorphy2
import string

from PostData.utils.model_saving import save_word
from PostData.utils.constants.smallWordsExcludingList import smallWordsExcludingList

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
            word = word.translate(str.maketrans('','',string.punctuation))
            save_word(word=word, model=Word)

            if  word not in smallWordsExcludingList:
                save_word(word=word, model=CleanWord)

class Tag(models.Model):
    tag = models.CharField(max_length=200)


class Word(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        ordering = ['-count']

class CleanWord(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        ordering = ['-count']

class PostDot(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=now)
    tags = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # pylint: disable=no-member
        super().save(*args, **kwargs)
        for word in self.content.lower().split():
            word = word.translate(str.maketrans('','',string.punctuation))
            save_word(word=word, model=WordDot)

            if  word not in smallWordsExcludingList:
                save_word(word=word, model=CleanWordDot)

class TagDot(models.Model):
    tag = models.CharField(max_length=200)


class WordDot(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        ordering = ['-count']

class CleanWordDot(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        ordering = ['-count']
