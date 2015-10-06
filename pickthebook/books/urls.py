__author__ = 'kvs'
#coding: utf-8
from django.conf.urls import patterns, url

from books.views import QuestionDetailView

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', QuestionDetailView.as_view()),

                       )