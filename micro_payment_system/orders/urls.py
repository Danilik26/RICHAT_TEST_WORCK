from django.urls import path

from . import views

urlpatterns =[
    path('all orders/', views.ShowAllOrders.as_view(), name = 'all_orders'),
    path('one_order/<int:order_id>/', views.ShowOneOrder.as_view(), name='one_order'),
    path('add_item/<int:item_id>/', views.AddItemToOrder.as_view(), name = "add_item")
]