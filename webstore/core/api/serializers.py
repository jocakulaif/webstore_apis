from rest_framework import serializers
from core.models import Product, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(allow_blank=True, allow_null=True, required=False)
#     description = serializers.CharField()
#     price = serializers.DecimalField(decimal_places=2, max_digits=10, required=False)
#     # image = serializers.ImageField(allow_empty_file=True)
#     stock_qty = serializers.IntegerField()
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Product.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         # instance.image = validated_data.get('image', instance.image)
#         instance.stock_qty = validated_data.get('stock_qty', instance.stock_qty)
#         instance.save()
#         return instance
