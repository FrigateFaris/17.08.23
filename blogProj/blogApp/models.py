from django.db import models
from django.shortcuts import reverse


# Create your models here.
class BlogModel(models.Model):
    user_id = models.IntegerField()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    count = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.author}'

    def get_absolute_url(self):
        return reverse('info', args=(self.pk,))
