# Generated by Django 4.2 on 2023-11-20 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_category_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategoryes'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='subcategory',
            new_name='parent',
        ),
    ]
