# Generated by Django 5.0.1 on 2024-01-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
