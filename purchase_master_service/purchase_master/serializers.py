from rest_framework import serializers
from .models import Purchase_master, Temp_purchase_details, Purchase_details

class PurchaseMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_master
        fields = ['id', 'invoice_no', 'invoice_date', 'supplier_id', 'status', 'purchase_date']


class TempPurchaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp_purchase_details
        fields = ['id', 'status', 'stampdatetime', 'item_id', 'rate', 'quantity', 'total']


class PurchaseDetailsSerializer(serializers.ModelSerializer):
    # Nested serializer for related Purchase_master
    purchase_master = PurchaseMasterSerializer(read_only=True)

    class Meta:
        model = Purchase_details
        fields = [
            'id',
            'status',
            'stampdatetime',
            'item',
            'rate',
            'quantity',
            'total',
            'fkey',  # ForeignKey field pointing to Purchase_master
            'purchase_master',
        ]
