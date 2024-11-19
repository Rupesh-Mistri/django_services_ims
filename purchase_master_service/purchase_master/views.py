from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase_master, Temp_purchase_details, Purchase_details
from .serializers import *
# Create your views here.

class Purchase(APIView):
    base_url="http://127.0.0.1"
    item_url=f'{base_url}:8001'
    supplier_url=f'{base_url}:8002'
    def get(self,requests):
        Temp_purchase_details.objects.all().delete()
        purchases = Purchase_master.objects.all()
        purchase_data = []
        
        for purchase in purchases:
            # item_response=requests.get(f"{self.item_url}/item/{purchase.supplier_id}/")
            # item_data = item_response.json() if item_response.status_code == 200 else {}

            supplier_response = requests.get(f"{self.supplier_url}/supplier/{purchase.supplier_id}/")
            supplier_data = supplier_response.json() if supplier_response.status_code == 200 else {}
        
            purchase_details=Purchase_details.objects.filter(fkey=purchase.id)
            aggregated_data = {
                "id": purchase.id,
                "click": purchase.id,
                "invoice_no": purchase.invoice_no,
                "invoice_date": purchase.invoice_date,
                "purchase_id": f"{purchase.id}-{purchase.invoice_date}",
                "supplier": supplier_data.get("name", "Unknown"),
                "details": purchase_details,
            }
            purchase_data.append(aggregated_data)

        return Response(purchase_data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer=PurchaseMasterSerializer()
        