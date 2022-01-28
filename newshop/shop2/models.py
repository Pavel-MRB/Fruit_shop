from django.db import models

# Create your models here.
class Item2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='img/')

    class Meta:
        verbose_name = 'Item2'
        verbose_name_plural = 'Items2'


