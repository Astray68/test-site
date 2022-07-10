from django.db import models


class Review(models.Model):
    name = models.CharField('Username', max_length=100)
    date_posted = models.DateTimeField('Date posting')
    message = models.TextField('Message', max_length=1000)
    STATUS_CHOICES = [
        (1, 'Moderation'),
        (2, 'Rejected'),
        (3, 'Published')
    ]
    status = models.SmallIntegerField('Status', choices=STATUS_CHOICES, default=1)
    is_deleted = models.BooleanField('Is_deleted', default=False)

    def __str__(self):
        return f"{self.name}-{self.date_posted}"

    def my_delete(self):
        self.is_deleted = True
        self.status = 2
        self.save()
        pass

    class Meta:
        verbose_name_plural = 'Reviews'
        verbose_name = 'Review'
