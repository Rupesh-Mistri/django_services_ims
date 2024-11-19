from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupplierSerializer
from .models import Supplier_master
# Create your views here.

class Supplier(APIView):
    def get(self, request):
        """
        Handles GET requests to retrieve all suppliers.
        """
        suppliers = Supplier_master.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)  # Use queryset
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handles POST requests to create a new supplier.
        """
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Handles PUT requests to update an existing supplier completely.
        """
        try:
            supplier = Supplier_master.objects.get(pk=pk)
        except Supplier_master.DoesNotExist:
            return Response({"error": "Supplier not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Handles PATCH requests to update part of an existing supplier.
        """
        try:
            supplier = Supplier_master.objects.get(pk=pk)
        except Supplier_master.DoesNotExist:
            return Response({"error": "Supplier not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(supplier, data=request.data, partial=True)  # Set partial=True
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Handles DELETE requests to delete an existing supplier.
        """
        try:
            supplier = Supplier_master.objects.get(pk=pk)
            supplier.delete()
            return Response({"message": "Supplier deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Supplier_master.DoesNotExist:
            return Response({"error": "Supplier not found"}, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, *args, **kwargs):
        """
        Handles OPTIONS requests to provide information about the API's capabilities.
        """
        response_data = {
            "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "description": "This endpoint manages supplier resources",
        }
        return Response(response_data, status=status.HTTP_200_OK)
