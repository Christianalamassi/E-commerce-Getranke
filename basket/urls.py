from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name="basket"),
    path('<basket_id>', views.add_basket, name="add_basket"),
    path('<basket_id>', views.fix_basket, name='fix_basket'),
]