#coding=utf-8

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class QuestionType(models.Model):
    """
    Тип: вопрос или ответ
    """
    type = models.IntegerField(default=1)
    description = models.CharField(max_length=10)
    def __str__(self):              # __unicode__ on Python 2
        return self.description
    def __unicode__(self):
        return self.description

class Question(MPTTModel):
    """
    Узел дерева вопросов и ответов, может быть как вопросом, так и ответом
    """
    q_text = models.CharField(max_length=100)
    position = models.IntegerField(default=0)
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name="Родитель", related_name="child")
    type = models.ForeignKey(QuestionType)

    class MPTTMeta:
        order_insertion_by=['q_text']

    def __str__(self):              # __unicode__ on Python 2
        return self.q_text
    def __unicode__(self):
        return self.q_text



class Author(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    fathername = models.CharField(max_length=45)
    biography = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=45)
    question = models.ForeignKey(Question)
    author = models.ManyToManyField(Author)

#MPTTModel.register(Question,)









