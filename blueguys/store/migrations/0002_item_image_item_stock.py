# Generated by Django 5.1.7 on 2025-04-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/'),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
