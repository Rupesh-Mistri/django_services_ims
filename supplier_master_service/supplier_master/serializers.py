from rest_framework import serializers
from .models import Supplier_master

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_master
        fields = '__all__'