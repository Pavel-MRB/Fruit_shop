from django.shortcuts import render
from .models import Item

def item_index(request):
    items=Item.objects.all()
    context={
        'items': items
    }
    return render(request, 'item_index.html',context)

def item_detail(request,pk):
    item=Item.objects.get(pk=pk)
    context={
        'item':item
    }

    return render(request,'item_detail.html',context)


