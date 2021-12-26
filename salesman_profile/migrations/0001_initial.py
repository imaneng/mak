# Generated by Django 4.0 on 2021-12-18 14:07

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesmanProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('telephone', models.CharField(max_length=11)),
                ('phone_number', models.CharField(max_length=11)),
                ('count', models.BigIntegerField()),
                ('Product', models.ManyToManyField(to='product.Product')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SalesmanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_import_product', models.DateTimeField(auto_now_add=True)),
                ('date_last_update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesman_profile.salesmanprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SalesmanAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=10)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesman_profile.salesmanprofile')),
            ],
        ),
        migrations.CreateModel(
            name='HistorySalesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_order', models.BigIntegerField()),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(to='product.Product')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesman_profile.salesmanprofile')),
            ],
        ),
    ]