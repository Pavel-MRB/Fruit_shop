from django.shortcuts import render
from .models import Item, Category

def item_index(request):
    #import pdb
    #pdb.set_trace()
    items = Item.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        items = items.filter(category=category_id)

    context={
        'items': items,
        'category': None if not category_id else Category.objects.get(pk=category_id)
    }
    return render(request, 'item_index.html',context)

def item_detail(request,pk):
    item=Item.objects.get(pk=pk)
    context={
        'item':item
    }

    return render(request,'item_detail.html',context)

def about_us(request):
    return render(request, 'about_us.html')
