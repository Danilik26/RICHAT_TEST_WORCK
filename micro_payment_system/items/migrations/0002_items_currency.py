# Generated by Django 5.1.6 on 2025-03-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='currency',
            field=models.CharField(choices=[('USD', 'US dollar'), ('AED', 'dirham')], db_default='USD', max_length=3),
        ),
    ]
