# Generated by Django 4.2 on 2023-11-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_dateform_sale_datefrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
