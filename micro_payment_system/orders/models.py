from django.db import models

from items.models import Items
# Create your models here.

class Orders(models.Model):

    items = models.ManyToManyField(Items)

    all_price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, db_default = 0)

    def __conversion_dirham_to_dollar(self, price):
        return price * 3.67

    def get_all_price(self):
        all_price = 0
        all_item = self.items.all()
        for item in all_item:

            if item.currency == Items.CHOICES_AED:
                item.price = self.__conversion_dirham_to_dollar(float(item.price))

            all_price += float(item.price)
        self.all_price = all_price
        return self.all_price

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('one_order', kwargs={'order_id':self.pk})
    
    class Meta:
        db_table = 'orders'
        db_table_comment = 'Table for orders'
        ordering = ['id']
        indexes = [models.Index(fields=['id'], name = 'idx_order_pk')]