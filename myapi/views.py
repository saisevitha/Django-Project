from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ecommerce
from .serializers import EcommerceSerializer

class ProductCreateView(APIView):
    def post(self, request):
        serializer = EcommerceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListView(APIView):
    def get(self, request):
        products = Ecommerce.objects.all()
        serializer = EcommerceSerializer(products, many=True)
        return Response(serializer.data)

class ProductUpdateView(APIView):
    def put(self, request, product_id):
        try:
            product = Ecommerce.objects.get(product_id=product_id)
        except Ecommerce.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EcommerceSerializer(product, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        try:
            product = Ecommerce.objects.get(product_id=product_id)
            product.delete()
            return Response({"product_id": product_id})
        except Ecommerce.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
