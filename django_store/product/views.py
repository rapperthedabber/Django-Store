from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class latestProducts(APIView):
    def get(self, request ,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


