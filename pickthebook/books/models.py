from django.db import models


class Question(models.Model):
    q_text = models.CharField(max_length=100)
    position = models.IntegerField


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


class Answer(models.Model):
    q_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question)


class Treepath(models.Model):
    level = models.IntegerField
    ancestor = models.ForeignKey(Question, related_name='+')
    descendant = models.ForeignKey(Question, related_name='+')



