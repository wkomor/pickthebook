from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item


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

    def get(self, request, format=None):
        item = self.get_object(request)
        nodes = item.get_children()
        node = ItemSerializer(nodes, many=True)
        children = nodes[0].get_children()
        answers = ItemSerializer(children, many=True)
        response = dict()
        response['node'] = node.data
        response['answers'] = answers.data
        return Response(response)


