from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

from .models import Question,  Author, Book


class QuestionDetailView(ListView):
    model = Question
    template_name = 'question_list.html'


class IndexView(TemplateView):
    template_name = 'index.html'
