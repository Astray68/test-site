# Generated by Django 4.0.5 on 2022-06-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Username'),
        ),
    ]