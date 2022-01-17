from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('Магазин овощей и фруктов. Адрес. г.Минск пр.Независимости,65')

