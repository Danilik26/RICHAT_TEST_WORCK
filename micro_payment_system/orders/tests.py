from django.test import TestCase
from django.urls import reverse

from .models import Orders
from .forms import AddItemToOrderForm

from items.models import Items

class AddItemOrderTestCase(TestCase):

    def setUp(self):
        i1 = Items.objects.create(name = 'кода', description = 'просто кола', price = 234.5, currency = Items.CHOICES_USD)
        i2 = Items.objects.create(name = 'спрайт', description = 'просто спрайт', price = 234.5, currency = Items.CHOICES_USD)
        Items.objects.create(name = 'фанта', description = 'просто фанта', price = 234.5, currency = Items.CHOICES_USD)

        o1 = Orders.objects.create()
        o1.items.set([i1, i2])

    def test_add_item(self):
        item = Items.objects.get(pk = 3)

        url = reverse('add_item', kwargs={'item_id':item.pk})

        AddItemToOrderForm.CHIOCES_ID_ORDERS = {'1':1}

        data = {
            'id_order':AddItemToOrderForm.CHIOCES_ID_ORDERS['1']
        }

        response = self.client.post(url, data)

        order = Orders.objects.get(pk = 1)



        self.assertEqual(response.status_code, 302)
        self.assertEqual(list(order.items.all()), [Items.objects.get(pk=1), Items.objects.get(pk=2), Items.objects.get(pk=3)])