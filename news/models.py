from django.db import models
from django.urls import reverse


class New(models.Model):
    title = models.CharField('Title new', max_length=100)
    short_content = models.TextField('Short content', max_length=20)
    full_content = models.TextField('Full content', max_length=10000)
    date_posted = models.DateTimeField('Date posting')
    image = models.ImageField('Image', upload_to='new/')
    slug = models.SlugField('URL', max_length=160, unique=True, null=True, db_index=True)
    is_deleted = models.BooleanField('Is_deleted', default=False)
    show_in_home = models.BooleanField('Show in home', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_new', args=[str(self.slug)])

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'New'
