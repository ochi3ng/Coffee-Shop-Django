# Generated by Django 5.1.3 on 2024-11-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_alter_category_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coffee',
        ),
    ]
