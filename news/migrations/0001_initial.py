# Generated by Django 4.0.5 on 2022-06-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title new')),
                ('short_content', models.TextField(max_length=20, verbose_name='Content')),
                ('date_posted', models.DateTimeField(verbose_name='Date posting')),
                ('image', models.ImageField(upload_to='new/', verbose_name='Image')),
                ('url', models.SlugField(max_length=160, verbose_name='URL')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is_deleted')),
            ],
        ),
    ]