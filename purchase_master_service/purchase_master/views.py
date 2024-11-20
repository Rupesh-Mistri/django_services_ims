from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase_master, Temp_purchase_details, Purchase_details
from .serializers import *
import requests

# Create your views here.


class Purchase(APIView):
    base_url = "http://192.168.1.5"
    item_url = f'{base_url}:8001'
    supplier_url = f'{base_url}:8002'

    def get(self, request,pk=None):
        Temp_purchase_details.objects.all().delete()
        if pk==None:
            purchases = Purchase_master.objects.all()
            purchase_data = []

            j=0
            for purchase in purchases:
                
                # print(f"{self.supplier_url}/supplier/{purchase.supplier_id}/")
                supplier_response = requests.get(f"{self.supplier_url}/supplier/{purchase.supplier_id}")
                supplier_data = supplier_response.json() if supplier_response.status_code == 200 else {}
                print("supplier_data",supplier_data)
                purchase_details = Purchase_details.objects.filter(fkey=purchase.id)
                aggregated_data = {
                    "id": purchase.id,
                    "invoice_no": purchase.invoice_no,
                    "invoice_date": purchase.invoice_date,
                    "purchase_id": f"{purchase.id}-{purchase.invoice_date}",
                    "supplier": supplier_data.get("name", "Unknown"),
                    "details": PurchaseDetailsSerializer(purchase_details, many=True).data,
                }
                # print(f"{self.item_url}/item/{aggregated_data['details'][j]['item']}")
                # item_response=requests.get(f"{self.item_url}/item/{aggregated_data['details'][j]['item']}")
                # item_data = item_response.json() if item_response.status_code == 200 else {}
                # aggregated_data['details'][j]['item']=item_data.get("item_name", "Unknown")
                # print(aggregated_data['details'][0]['item'])
                purchase_data.append(aggregated_data)
                j=j+1
        else:
            purchase = Purchase_master.objects.filter(pk=pk).first()
            purchase_details = Purchase_details.objects.filter(fkey=purchase.id)

            supplier_response = requests.get(f"{self.supplier_url}/supplier/{purchase.supplier_id}")
            supplier_data = supplier_response.json() if supplier_response.status_code == 200 else {}
            print("supplier_data",supplier_data)
            purchase_data=[{
                    "id": purchase.id,
                    "invoice_no": purchase.invoice_no,
                    "invoice_date": purchase.invoice_date,
                    "purchase_id": f"{purchase.id}-{purchase.invoice_date}",
                    "supplier": supplier_data.get("name", "Unknown"),
                    "details": PurchaseDetailsSerializer(purchase_details, many=True).data,
                }]
        return Response(purchase_data, status=status.HTTP_200_OK)

    def post(self, request):
        # Extract master data
        master_data = request.data.get("purchase_master", {})
        details_data = request.data.get("purchase_details", {})

        # Validate and save Purchase_master
        master_serializer = PurchaseMasterSerializer(data=master_data)
        if master_serializer.is_valid():
            master_instance = master_serializer.save()
        else:
            return Response(master_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Validate and save Purchase_details
        for detail_key, detail_value in details_data.items():
            detail_value["fkey"] = master_instance.id  # Associate with the saved master record
            detail_serializer = PurchaseDetailsSerializer(data=detail_value)
            if detail_serializer.is_valid():
                detail_serializer.save()
            else:
                return Response(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Purchase data saved successfully!"}, status=status.HTTP_201_CREATED)

