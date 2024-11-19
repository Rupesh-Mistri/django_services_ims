from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer
from rest_framework import status
from .models import Item_master
def index(request):
    return HttpResponse('Hello')


class Item(APIView):
    def get(self, request,pk=None):
        """
        Handles GET requests to retrieve all items.
        """
        if pk is None:
            items = Item_master.objects.all()
            serializer = ItemSerializer(items, many=True)
        else:
            try:
                supplier = Item_master.objects.get(pk=pk)  # Get supplier by primary key
                serializer = ItemSerializer(supplier)  # Serialize single object
            except Item_master.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handles POST requests to create a new item.
        """
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Handles PUT requests to update an existing item completely.
        """
        try:
            item = Item_master.objects.get(pk=pk)
        except Item_master.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Handles PATCH requests to update part of an existing item.
        """
        try:
            item = Item_master.objects.get(pk=pk)
        except Item_master.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Handles DELETE requests to delete an existing item.
        """
        try:
            item = Item_master.objects.get(pk=pk)
            item.delete()
            return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Item_master.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    def options(self, request, *args, **kwargs):
        """
        Handles OPTIONS requests to provide information about the API's capabilities.
        """
        response_data = {
            "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "description": "This endpoint manages item resources",
        }
        return Response(response_data, status=status.HTTP_200_OK)
