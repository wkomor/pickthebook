__author__ = 'kvs'
#coding: utf-8
from django.conf.urls import patterns, url

from books.views import QuestionDetailView, IndexView

urlpatterns = patterns('',
                       url(r'^/question', QuestionDetailView.as_view(), name='question',),
                       url(r'^$', IndexView.as_view(),),
                       )