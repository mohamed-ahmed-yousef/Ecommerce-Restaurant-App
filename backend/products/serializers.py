from rest_framework import serializers
from .models import ProductImage, category, Discount, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('id', 'name')

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'code', 'percentage', 'start_date', 'end_date')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    class Meta:
           model = Product
           fields = ['id','available_quantity', 'name', 'description', 'price','category','discount','images']

           
           
           
    def create(self, validated_data):
            images_data = self.context['request'].FILES.getlist('images')
            product = Product.objects.create(**validated_data)
            print('*'*100)
            # print(images_data)
            for image in images_data:
                print(product,image)
                ProductImage.objects.create(product=product, image=image)

            return product

