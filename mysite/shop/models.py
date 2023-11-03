from django.db import models


def image_category_directory_path(instance: "Category", filename: str) -> str:
    return "categories/category_{slug}/images/{filename}".format(
        slug=instance.slug,
        filename=filename,
    )

def image_product_directory_path(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to=image_category_directory_path)
    class Meta:
        ordering = ['-title']
        indexes = [
            models.Index(fields=['title'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(null=True, blank=True,
                              upload_to=image_product_directory_path)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    count = models.PositiveIntegerField(verbose_name='count')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

        def __str__(self) -> str:
            return self.name
