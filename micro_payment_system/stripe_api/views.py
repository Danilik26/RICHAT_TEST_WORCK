from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from django.urls import reverse

from micro_payment_system.settings import STRIPE_SECRET_KEY

from items.models import Items

from orders.models import Orders

import stripe


def conversion_dirham_to_dollar(price):
    return price * 3.67



class MakeStripeSessionForOneItem(APIView):

    def get(self, request, item_id):
        item = Items.objects.get(pk = item_id)
        item_curency = item.currency
        stripe.api_key = STRIPE_SECRET_KEY
        if item_curency == Items.CHOICES_USD:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data" :{
                            'currency':'usd',
                            'product_data':{
                                'name':item.name
                            },
                            'unit_amount':int(item.price)*100,
                        },
                        'quantity':1
                    }
                ],
            mode="payment",
            success_url=f'http://127.0.0.1:8000/{reverse('successful_purchase')}',
            cancel_url=f'http://127.0.0.1:8000/{reverse('cancel_purchase')}'
            )
            return Response({'sessionId':session.id}, status = status.HTTP_200_OK)
        elif item_curency == Items.CHOICES_AED:
            session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data" :{
                            'currency':'aed',
                            'product_data':{
                                'name':item.name
                            },
                            'unit_amount':int(item.price)*100,
                        },
                        'quantity':1
                    }
                ],
            mode="payment",
            success_url=f'http://127.0.0.1:8000/{reverse('successful_purchase')}',
            cancel_url=f'http://127.0.0.1:8000/{reverse('cancel_purchase')}'
            )
            return Response({"sessionId":session.id}, status = status.HTTP_200_OK)


class MakeStripeSessionForOrder(APIView):

    def get(self, request, order_id):
        order = Orders.objects.get(pk = order_id)
        
        stripe.api_key = STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(line_items=[
                {
                    "price_data" :{
                        'currency':'usd',
                        'product_data':{
                            'name':f'order id -> {order.pk}' 
                        },
                        'unit_amount':int(order.get_all_price())*100,
                    },
                    'quantity':1
                }
            ],
        mode="payment",
        success_url=f'http://127.0.0.1:8000/{reverse('successful_purchase')}',
        cancel_url=f'http://127.0.0.1:8000/{reverse('cancel_purchase')}'
        )
        return Response({'sessionId':session.id})
    
def successful_purchase(request):
    return render(request, 'stripe_api/successful_purchase.html')

def cancel_purchase(request):
    return render(request, 'stripe_api/cancel_purchase.html')