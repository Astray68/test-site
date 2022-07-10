from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Name_category', max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField('Image', upload_to='category/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_info', kwargs={'category_slug': self.slug})

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass


class Promotion(models.Model):
    title = models.CharField('Title', max_length=20)
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    content = models.TextField('Content', blank=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('promotion_info', kwargs={'promotion_slug': self.slug})

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'


class Product(models.Model):
    name = models.CharField('Name_product', max_length=100)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)
    image = models.ImageField('Image', upload_to='product/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    content = models.TextField('Content', max_length=1000)
    characteristics = models.TextField('Characteristics', max_length=2000)
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    is_deleted = models.BooleanField('Is_deleted', default=False)
    promotion = models.ManyToManyField(Promotion, default=None, verbose_name='Promotion')
    show_in_home = models.BooleanField('Show in home', default=False)

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_info', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
