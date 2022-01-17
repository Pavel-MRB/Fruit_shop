from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=20)
    image=models.FileField(upload_to='img/')

