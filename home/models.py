from django.db import models


class Banner(models.Model):
    title = models.CharField('Title new', max_length=35)
    image = models.ImageField('Image', upload_to='banner/')
    is_deleted = models.BooleanField('Is_deleted', default=False)
    show_in_home = models.BooleanField('Show in home', default=False)

    def __str__(self):
        return self.title

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    class Meta:
        verbose_name_plural = 'Banners'
        verbose_name = 'Banner'
