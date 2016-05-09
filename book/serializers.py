from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):

    itemtype = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'text', 'parent', 'itemtype')

    def get_itemtype(self, obj):
        return obj.get_itemtype_display()


