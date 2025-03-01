from django.shortcuts import render, redirect
from django.views import View

from .models import Orders
from .forms import AddItemToOrderForm

from micro_payment_system.settings import STRIPE_PUBLIC_KEY

# Create your views here.

class ShowOneOrder(View):

    def get(self, request, order_id):
        order = Orders.objects.filter(pk = order_id).select_related()[0]
        items_in_order = order.items.all()
        context = {
            'order_data':order,
            'items_in_order':items_in_order,
            'key':STRIPE_PUBLIC_KEY
        }

        return render(request, 'orders/show_order.html', context)
    

class ShowAllOrders(View):

    def get(self, request):
        orders = Orders.objects.all()
        context = {
            'orders':orders
        }
        return render(request, 'orders/show_all_orders.html', context)
    

class AddItemToOrder(View):

    def get(self, request, item_id):
        form = AddItemToOrderForm()
        context = {
            'form':form
        }
        return render(request, 'orders/add_item_to_order.html', context)
    
    def post(self, request, item_id):
        form = AddItemToOrderForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form.save(item_id, form_data)
            return redirect('all_items')
        else:
            return redirect('all_items')