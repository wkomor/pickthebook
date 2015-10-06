from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Question, Answer, Author, Book

class QuestionDetailView(ListView):
    model = Question
    template_name = 'question_list.html'

