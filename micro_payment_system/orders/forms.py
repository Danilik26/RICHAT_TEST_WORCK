from django import forms

from .models import Orders


class AddItemToOrderForm(forms.Form):
    CHOISEC_ORDERS_ID = {f'{x.id}':x.pk for x in Orders.objects.all()}
    print(CHOISEC_ORDERS_ID)

    id_order = forms.ChoiceField(choices = CHOISEC_ORDERS_ID)

    def save(self, item_id, cleaned_data):
        order = Orders.objects.get(pk = cleaned_data['id_order'])
        order.items.add(item_id)
        return order.save()