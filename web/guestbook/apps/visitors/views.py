from django.shortcuts import render, redirect
from .models import Item
from redis import Redis


#redis = Redis(host='redis', port=6379)


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return render(request, 'thankyou.html', {})
    items = Item.objects.all()
    #counter = redis.incr('counter')
    counter = 33
    return render(request, 'home.html', {'items': items, 'counter': counter})

def visitors(request):
    items = Item.objects.all()
    counter = 33
    return render(request, 'visitors.html', {'items': items, 'counter': counter})
