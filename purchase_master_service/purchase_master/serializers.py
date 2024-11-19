from rest_framework import serializers
from .models import Purchase_master, Temp_purchase_details, Purchase_details

class PurchaseMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_master
        fields = ['id', 'invoice_no', 'invoice_date', 'supplier_id', 'status', 'purchase_date']
# {
#     "invoice_no":"1234",
#     "invoice_date":"2024-11-23",
#     "supplier_id":1,
#     "status":1,
#     "purchase_date":"2024-11-23"
# }

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
# {
#     "status":1,
#     "stampdatetime":"2024-11-23",
#     "item":1,
#     "rate":20,
#     "quantity":10,
#     "total":200,
#     "fkey":1,
#     "purchase_master":1
# }

{
    "purchase_master":{
            "invoice_no":"1234",
            "invoice_date":"2024-11-23",
            "supplier_id":1,
            "status":1,
            "purchase_date":"2024-11-23"
        },
    "purchase_details":{
       "item1":{ "status":1,
        "stampdatetime":"2024-11-23",
        "item":1,
        "rate":20,
        "quantity":10,
        "total":200,
        "fkey":1,
        "purchase_master":1
       },
        "item2":{ "status":1,
        "stampdatetime":"2024-11-23",
        "item":2,
        "rate":30,
        "quantity":10,
        "total":300,
        "fkey":1,
        "purchase_master":1
       }
    }
}