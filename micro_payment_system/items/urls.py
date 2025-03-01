from django.urls import path

from . import views

urlpatterns = [
    path("item/<int:item_id>", views.ShowOneItem.as_view(), name = "one_item"),
    path("items/", views.ShowAllItems.as_view(), name = "all_items")
]   