from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Purchase_master, Temp_purchase_details, Purchase_details
from .serializers import *
import requests

# Create your views here.

IS_LOCAL=True

class Purchase(APIView):
    base_url ="http://127.0.0.1" if IS_LOCAL else "http://192.168.1.5" 
    item_url = f'{base_url}:8001'
    supplier_url = f'{base_url}:8002'

    def get_supplier_data(self, supplier_id):
        token = get_supplier_service_token()
        # print("Token",token)
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.supplier_url}/supplier/{supplier_id}", headers=headers)

        if response.status_code == 200:
            # print(response.json())
            return response.json()
        else:
            return {"error": "Unable to fetch supplier data"}
    
    def get(self, request, pk=None):
        # Fetch supplier data using the above method
        if pk is None:
            purchases = Purchase_master.objects.all()
            purchase_data = []
            for purchase in purchases:
                supplier_data = self.get_supplier_data(purchase.supplier_id)
                print(supplier_data)
                purchase_details = Purchase_details.objects.filter(fkey=purchase.id)
                aggregated_data = {
                    "id": purchase.id,
                    "invoice_no": purchase.invoice_no,
                    "invoice_date": purchase.invoice_date,
                    "purchase_id": f"{purchase.id}-{purchase.invoice_date}",
                    "supplier": supplier_data.get("name", "Unknown"),
                    "details": PurchaseDetailsSerializer(purchase_details, many=True).data,
                }
                purchase_data.append(aggregated_data)
        else:
            purchase = Purchase_master.objects.filter(pk=pk).first()
            supplier_data = self.get_supplier_data(purchase.supplier_id)
            purchase_details = Purchase_details.objects.filter(fkey=purchase.id)
            purchase_data = [{
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



def get_supplier_service_token():
    base_url ="http://127.0.0.1" if IS_LOCAL else "http://192.168.1.5" 
    # Replace with actual credentials
    response = requests.post(
        f"{base_url}:8002/api/token/",
        data={"username": "rupesh", "password": "1234"}
    )
    # print("RRRRRRRRRRR",response.json())
    if response.status_code == 200:
        return response.json().get("access")
    else:
        raise Exception("Failed to obtain token for supplier service")