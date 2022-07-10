from django.db import models


class Contact(models.Model):
    first_name = models.CharField('Fist name', max_length=20)
    last_name = models.CharField('Last name', max_length=25)
    email = models.EmailField('Email', max_length=254)
    phone = models.CharField('Phone', max_length=17)
    message = models.TextField('Message', max_length=1000)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return self.email

    def my_delete(self):
        self.is_deleted = True
        self.save()
        pass

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'
