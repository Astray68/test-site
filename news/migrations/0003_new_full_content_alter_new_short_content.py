# Generated by Django 4.0.5 on 2022-06-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_options_remove_new_url_new_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='full_content',
            field=models.TextField(default=0, max_length=10000, verbose_name='Full content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='short_content',
            field=models.TextField(max_length=20, verbose_name='Short content'),
        ),
    ]