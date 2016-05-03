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

    item_type = models.PositiveSmallIntegerField(choices=ITEM_TYPE, db_index=True)
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               verbose_name="Parent", related_name='child', db_index=True)
    image = models.ImageField(blank=True, null=True)
    is_positive = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'item_type'
        order_insertion_by=['title']


mptt.register(Item,)
