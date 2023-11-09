# Generated by Django 4.2 on 2023-11-09 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_rename_dateform_sale_datefrom'),
        ('myauth', '0002_alter_profile_options_remove_profile_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200, verbose_name='address')),
                ('city', models.CharField(default='', max_length=200, verbose_name='city')),
                ('deliveryType', models.CharField(default='', max_length=150, verbose_name='type delivery')),
                ('paymentType', models.CharField(default='', max_length=150, verbose_name='type payment')),
                ('totalCost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='total cost')),
                ('status', models.CharField(default='', max_length=150, verbose_name='status')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
                ('products', models.ManyToManyField(related_name='orders', to='shop.product', verbose_name='products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myauth.profile', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='CountProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product')),
            ],
        ),
    ]
