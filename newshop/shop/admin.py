from django.contrib import admin
from .models import Item, Category

admin.site.register(Item)
# Register your models here.
admin.site.register(Category)