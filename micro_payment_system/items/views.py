from django.shortcuts import render, redirect
from django.views import View

from .models import Items

from micro_payment_system.settings import STRIPE_PUBLIC_KEY



class ShowOneItem(View):

    def get(self, request, item_id):
        item = Items.objects.get(pk = item_id)
        context = {
            'item':item,
            "pub_key":STRIPE_PUBLIC_KEY
        }
        return render(request, 'items/tmp_one_item.html', context)


class ShowAllItems(View):

    def get(self, request):
        items = Items.objects.all()
        context = {
            'items':items
        }
        return render(request, 'items/show_all_items.html', context)