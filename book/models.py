from __future__ import unicode_literals

from django.db import models
import mptt
from mptt.models import MPTTModel


# Create your models here.


class Item(MPTTModel):
    """

    """
    QUESTION = 0
    ANSWER = 1
    BOOK = 2
    ITEM_TYPE = ((QUESTION, 'Question'), (ANSWER, 'Answer'), (BOOK, 'Book'))

    itemtype = models.PositiveSmallIntegerField(choices=ITEM_TYPE,
                                                db_index=True,
                                                default=QUESTION)
    slag = models.SlugField(max_length=16, allow_unicode=True, null=True,
                            blank=True)
    text = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name="Parent", related_name='child',
                               db_index=True)

    is_positive = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.text

    class MPTTMeta:
        level_attr = 'item_type'
        order_insertion_by = ['text']


class Genre(models.Model):
    """

    """
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """

    """
    title = models.CharField(max_length=1024, db_index=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True,
                              db_index=True)
    item = models.ForeignKey(Item, related_name='books', null=True)
    genre = models.ManyToManyField(Genre, db_index=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


mptt.register(Item, )
