from django.core.exceptions import ObjectDoesNotExist
import pymorphy2
import string

morph = pymorphy2.MorphAnalyzer()

def save_word(word, model):
    wd = morph.parse(word)[0].normal_form

    try:
        word_in_db = model.objects.get(word=wd)
        word_in_db.count += 1
        word_in_db.save(update_fields=['count'])
    except ObjectDoesNotExist:
        w = model(word=wd, count = 1)
        w.save()
