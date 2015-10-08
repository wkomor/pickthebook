#coding=utf-8
from django.db import models


class QuestionType(models.Model):
    """
    Тип: вопрос или ответ
    """
    type = models.BooleanField


class Question(models.Model):
    """
    Узел дерева вопросов и ответов, может быть как вопросом, так и ответом
    """
    q_text = models.CharField(max_length=100)
    position = models.IntegerField
    type = models.ForeignKey(QuestionType)


class Ancestor(models.Model):
    """
        Класс для хранения вопроса-предка
    """
    ancestor = models.ForeignKey(Question, related_name='+')
    descendant = models.IntegerField


class Descendant(models.Model):
    """
        Класс для хранения вопроса-потомка
    """
    descendant = models.ForeignKey(Question, related_name='+')


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










