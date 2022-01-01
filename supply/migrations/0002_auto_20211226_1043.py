# Generated by Django 3.2.9 on 2021-12-26 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_property'),
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesmanproduct',
            old_name='count',
            new_name='amount',
        ),
        migrations.CreateModel(
            name='SalesManProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supply.salesmanproduct')),
                ('prop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.property')),
            ],
        ),
    ]