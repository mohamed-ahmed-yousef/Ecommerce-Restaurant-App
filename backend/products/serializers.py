from rest_framework import serializers
from .models import  Category, ProductImage, Discount, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  '__all__'
        # fields = ('id', 'name')

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields ='__all__'
        # fields = ('id', 'code', 'percentage', 'start_date', 'end_date')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    class Meta:
           model = Product
           fields = '__all__'
        #    fields = ['id','available_quantity', 'name', 'description', 'price','category','discount','restaurant','images']

           
    def create(self, validated_data):
            images_data = self.context['request'].FILES.getlist('images')
            product = Product.objects.create(**validated_data)
            for image in images_data:
                ProductImage.objects.create(product=product, image=image)

            return product

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images_data =ProductImageSerializer(ProductImage.objects.filter(product=instance),many=True).data
        data['images'] = images_data
        return data

