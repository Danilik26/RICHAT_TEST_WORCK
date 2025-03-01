from django.db import models


# Create your models here.

class Items(models.Model):
    CHOICES_USD = 'USD'
    CHOICES_AED = 'AED'

    CURENCY_CHOICES = {
        CHOICES_USD:'US dollar',
        CHOICES_AED:'dirham',
    }

    name = models.CharField(max_length = 100)
    description = models.TextField()

    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    currency = models.CharField(max_length = 3, choices = CURENCY_CHOICES, db_default = CHOICES_USD)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('one_item', kwargs={"item_id":self.pk})
    
    class Meta:
        db_table = 'items'
        db_table_comment = 'Table for items'
        ordering = ['id']
        indexes = [models.Index(fields=['id'], name = 'idx_item_pk')]