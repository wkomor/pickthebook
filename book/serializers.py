from rest_framework import serializers
from .models import Item, Book


class ItemSerializer(serializers.ModelSerializer):

    itemtype = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id', 'text', 'parent', 'itemtype', 'slag')

    def get_itemtype(self, obj):
        return obj.get_itemtype_display()


class BookSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'genre', 'image')
