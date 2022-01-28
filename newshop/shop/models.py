from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

# Create your models here.
class Item(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default="1")
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=20)
    image=models.FileField(upload_to='img/')

    def __str__(self):
        return self.title

