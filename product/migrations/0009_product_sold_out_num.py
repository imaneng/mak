# Generated by Django 3.2.9 on 2022-01-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_out_num',
            field=models.BigIntegerField(null=True),
        ),
    ]