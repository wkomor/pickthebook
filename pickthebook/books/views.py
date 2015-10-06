from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Question, Answer, Author, Book

class QuestionDetailView(DetailView):
    model = Question
    slug_field = 'q_text'

