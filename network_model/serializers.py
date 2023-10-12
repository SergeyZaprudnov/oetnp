from rest_framework import serializers

from network_model.models import Product, Structure


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        only_fields = ('id', 'name', 'model', 'release_date')


class StructureSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, required=False)
    supplier = serializers.SlugRelatedField(slug_field='name', queryset=Structure.objects.all())

    class Meta:
        model = Structure
        fields = '__all__'
        only_fields = ('debt', 'created')


class StructureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'
