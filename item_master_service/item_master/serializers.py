from rest_framework import serializers
from .models import Item_master

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_master
        fields = '__all__'