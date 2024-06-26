from django.urls import path
from . import views

urlpatterns = [
    path('basket', views.basket, name="basket"),
    path('<basket_id>', views.add_basket, name="add_basket"),
]