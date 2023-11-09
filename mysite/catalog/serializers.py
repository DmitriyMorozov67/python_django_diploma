from rest_framework import serializers
from .models import Category, CategoryIcon


class CategoryIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryIcon
        fields = ['id', 'src', 'alt']


class SubSerializer(serializers.ModelSerializer):
    image = CategoryIconSerializer(many=False, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    image= CategoryIconSerializer(many=False, required=False)
    subcategory = SubSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'
