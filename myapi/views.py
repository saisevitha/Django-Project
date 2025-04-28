

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ecommerce

@api_view(['POST'])
def create_product(request):
    data = request.data
    product = Ecommerce.objects.create(
        product_name=data.get('product_name'),
        price=data.get('price'),
        description=data.get('description')
    )
    return Response({
        "product_id": product.product_id,
        "product_name": product.product_name,
        "price": str(product.price),
        "description": product.description
    }, status=status.HTTP_201_CREATED)

    
@api_view(['GET'])
def read_products(request):
    products = Ecommerce.objects.all()
    product_list = []
    for product in products:
        product_list.append({
            "product_id": product.product_id,
            "product_name": product.product_name,
            "price": str(product.price),
            "description": product.description
        })
    return Response(product_list)

@api_view(['PUT'])
def update_product(request, product_id):
    try:
        product = Ecommerce.objects.get(product_id=product_id)
        data = request.data
        product.product_name = data.get('product_name')
        product.price = data.get('price')
        product.description = data.get('description')
        product.save()
        return Response({
            "product_id": product.product_id,
            "product_name": product.product_name,
            "price": str(product.price),
            "description": product.description
        })
    except Ecommerce.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = Ecommerce.objects.get(product_id=product_id)
        product.delete()
        return Response({"product_id": product_id})
    except Ecommerce.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

