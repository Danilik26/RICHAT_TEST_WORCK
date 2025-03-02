from django.urls import path

from . import views

urlpatterns = [
    path("<int:item_id>", views.MakeStripeSessionForOneItem.as_view()),
    path("order/by/<int:order_id>", views.MakeStripeSessionForOrder.as_view(),),
    path("successful_purchase", views.successful_purchase, name = 'successful_purchase'),
    path("cancel_purchase", views.cancel_purchase, name = 'cancel_purchase'),
]