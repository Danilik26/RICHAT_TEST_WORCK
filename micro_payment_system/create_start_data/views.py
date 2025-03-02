from django.shortcuts import redirect

from items.models import Items
from orders.models import Orders

# Create your views here.

def create_start_data(self):
    Items.objects.create(name = 'Carrot' , description = 'Sweet carrot from the Alpine mountains', price = 999.9, currency = Items.CHOICES_USD)
    Items.objects.create(name = 'Cucumber ' , description = 'Cucumber grown to classical music has a special watery taste', price = 100.9, currency = Items.CHOICES_USD)
    Items.objects.create(name = 'Strawberry' , description = 'They say that strawberries among berries are like Queen Victoria among queens', price = 400, currency = Items.CHOICES_AED)
    Items.objects.create(name = 'Broccoli' , description = 'We ourselves are shocked, but they can be delicious too', price = 100.5, currency = Items.CHOICES_AED)

    Orders.objects.create()
    Orders.objects.create()
    return redirect('all_items')