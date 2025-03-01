from django.urls import path

from . import views

urlpatterns = [
    path("<int:item_id>", views.MakeStripeSessionForOneItem.as_view()),
    path("order/by/<int:order_id>", views.MakeStripeSessionForOrder.as_view(),)
]