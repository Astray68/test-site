# Generated by Django 4.0.5 on 2022-07-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_category_level_remove_category_lft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show_in_home',
            field=models.BooleanField(default=False, verbose_name='Show in home'),
        ),
    ]