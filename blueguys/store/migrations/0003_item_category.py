# Generated by Django 5.1.7 on 2025-04-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_item_image_item_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
