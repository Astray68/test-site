# Generated by Django 4.0.5 on 2022-07-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is_deleted'),
        ),
    ]