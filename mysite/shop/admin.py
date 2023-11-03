from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'count', 'created', 'updated']
    list_filter = ['count', 'created', 'updated']
    list_editable = ['price', 'count']
    prepopulated_fields = {'slug': ('name',)}
