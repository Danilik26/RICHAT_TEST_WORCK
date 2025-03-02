from django import forms

from .models import Orders

from django.db.utils import ProgrammingError


class AddItemToOrderForm(forms.Form):

    try:
        CHIOCES_ID_ORDERS = {f'{x.id}':x.pk for x in Orders.objects.all()}
    except ProgrammingError:
        CHIOCES_ID_ORDERS = {}

    id_order = forms.ChoiceField(choices = CHIOCES_ID_ORDERS)
    

    def save(self, item_id, cleaned_data):
        order = Orders.objects.get(pk = cleaned_data['id_order'])
        order.items.add(item_id)
        return order.save()