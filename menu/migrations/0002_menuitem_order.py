# Generated by Django 4.0.5 on 2022-06-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=500, verbose_name='Order'),
        ),
    ]
