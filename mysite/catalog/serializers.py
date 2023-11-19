from rest_framework import serializers
from .models import Category, CategoryIcon
from rest_framework import pagination




class CategoryIconSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()
    alt = serializers.CharField(default='pictures')
    
    class Meta:
        model = CategoryIcon
        fields = ['src', 'alt']
    
    def get_src(self, obj):
        if obj.image:
            return obj.image.url
        return None  


class SubSerializer(serializers.ModelSerializer):
    image = CategoryIconSerializer(many=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class CategorySerializer(serializers.ModelSerializer):
    image = CategoryIconSerializer(many=False, required=False)
    subcategories= SubSerializer(many=True, required=False)
    # subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'subcategories']

    # def get_subcategories(self, instance):
    #     return Category.objects.get('subcategories').all()

        

