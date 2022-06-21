from django.db import models
# Create your models here.
from django.urls import reverse


class New(models.Model):
    title = models.CharField('Title new', max_length=100)
    short_content = models.TextField('Content', max_length=20)
    date_posted = models.DateTimeField('Date posting')
    image = models.ImageField('Image', upload_to='new/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_new', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'New'
