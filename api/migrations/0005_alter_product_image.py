# Generated by Django 5.0.1 on 2024-01-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]