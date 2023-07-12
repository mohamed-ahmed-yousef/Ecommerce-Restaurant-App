from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import ProductImage, category, Discount, Product
from .serializers import CategorySerializer, DiscountSerializer, ProductImageSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    # def create(self, request, *args, **kwargs):
    #     form = ProductForm(request.data)
    #     if form.is_valid():
    #         product = form.save()
    #         serializer = self.serializer_class(product)
    #         return response(serializer.data)
    #     else:
    #         return response(form.errors, status=400)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     images = request.FILES.getlist('images')

    #     product = serializer.save()

    #     for image in images:
    #         ProductImage.objects.create(product=product, image=image)

    #     headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

