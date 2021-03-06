# Generated by Django 4.0.5 on 2022-06-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.RemoveField(
            model_name='new',
            name='url',
        ),
        migrations.AddField(
            model_name='new',
            name='slug',
            field=models.SlugField(max_length=160, null=True, unique=True, verbose_name='URL'),
        ),
    ]
