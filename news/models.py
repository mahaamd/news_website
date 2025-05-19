from django.db import models
from django.utils import timezone
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.CharField(max_length=50)
    source = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_time']
