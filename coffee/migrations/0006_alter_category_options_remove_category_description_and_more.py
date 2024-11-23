# Generated by Django 5.1.3 on 2024-11-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_coffee_alter_category_options_category_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
