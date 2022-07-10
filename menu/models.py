from django.db import models


class MenuItem(models.Model):
    order = models.IntegerField('Order', default=500)
    title = models.CharField('Title', max_length=25)
    url = models.CharField('Link URL', max_length=100)
    show_in_footer = models.BooleanField('Show in footer', default=False)
    login_required = models.BooleanField('Login required', default=False)
    anonymous_only = models.BooleanField('anonymous_only', default=False)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return self.title

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    class Meta:
        verbose_name_plural = 'Menu items'
        verbose_name = 'Menu item'
