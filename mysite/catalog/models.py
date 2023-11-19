from django.db import models

def icon_category_directory_path(instanse: "CategoryIcon", filename: str) -> str:
    if instanse.category.subcategory:
        return 'catalog/icons/{subcategory}/{category}/{filename}'.format(
            subcategory=instanse.category.subcategory,
            category=instanse.category,
            filename=filename
        )
    else:
        return 'catalog/icons/{category}/{filename}'.format(
            category=instanse.category,
            filename=filename
        )


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    active = models.BooleanField(default=False)
    subcategory = models.ForeignKey('self', on_delete=models.PROTECT,
                                    blank=True, null=True,
                                    related_name='subcategories')
    favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['pk',]

    def href(self):
        return f'catalog/{self.pk}'
    
    def __str__(self):
        return self.title
    

class CategoryIcon(models.Model):
    image = models.FileField(upload_to=icon_category_directory_path,
                           max_length=400)
    category = models.OneToOneField(Category, on_delete=models.CASCADE,
                                    related_name='icon', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Category icon'
        verbose_name_plural = 'Category icons'
        ordering = ['pk',]

    def alt(self):
        return self.category.title
    
    def href(self):
        return self.image
    
    def __str__(self):
        return 'icon of {title}'.format(title=self.category.title)