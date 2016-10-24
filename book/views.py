from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item


class IndexView(TemplateView):
    template_name = 'index.html'

class ItemList(generics.ListAPIView):
    """
    API endpoint that represents a list of items.
    """
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

