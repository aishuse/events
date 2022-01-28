from django.db import models

from authapp.models import MyUser


class Event(models.Model):

    NOT_PUBLISHED = 'not_published'
    PUBLISHED = 'published'
    options = (
        ('NOT_PUBLISHED', 'not_published'),
        ('PUBLISHED', 'published')
    )

    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=120, verbose_name='Name of the Event')
    venue = models.CharField(max_length=120)
    date = models.DateField(verbose_name='Date of Event')
    start_time = models.TimeField()
    end_time = models.TimeField()
    host = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=options, default='NOT_PUBLISHED')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name