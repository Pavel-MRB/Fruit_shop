from django.shortcuts import render
from .models import Item2

def item2_index(request):
    items2=Item2.objects.all()
    context={
        'items2': items2
    }
    return render(request, 'item2_index.html',context)

def item2_detail(request,pk):
    item2=Item2.objects.get(pk=pk)
    context={
        'item2':item2
    }

    return render(request,'item2_detail.html',context)

def about_us(request):
    return render(request, 'about_us.html')
