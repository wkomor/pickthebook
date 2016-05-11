from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .serializers import ItemSerializer, BookSerializer
from .models import Item, Book


class ItemList(generics.ListAPIView):
    """
    API endpoint that represents a list of items.
    """
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.root_nodes()


class ItemDetail(APIView):
    """
    Retrieve a node with his children.
    """
    def get_object(self, request):
        try:
            return Item.objects.get(pk=request.GET.get('id'))
        except Item.DoesNotExist:
            raise Http404

    def get_book(self, item):
        try:
            return Book.objects.get(item=item)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        item = self.get_object(request)
        child = item.get_children().first()
        response = dict()
        if child:
            response['node'] = ItemSerializer(child).data
            if child.itemtype == Item.BOOK:
                response['book'] = BookSerializer(self.get_book(child)).data
            children = child.get_children()
            if children:
                response['answers'] = ItemSerializer(children, many=True).data
        else:
            raise Http404
        return Response(response)


