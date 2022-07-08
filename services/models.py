from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
#TODO: переделать на mptt

class Category(models.Model):
    name = models.CharField('Name_category', max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Image', upload_to='category/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField('Name_product', max_length=100)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)
    image = models.ImageField('Image', upload_to='product/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    content = models.TextField('Content', max_length=1000)
    characteristics = models.TextField('Characteristics', max_length=2000)
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    is_deleted = models.BooleanField('Is_deleted', default=False)
    #promotion

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'


class Promotion(models.Model):
    title = models.CharField('Title', max_length=20)
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    content = models.TextField('Content', blank=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('promotion_info', kwargs={'promotion_slug': self.slug})

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
