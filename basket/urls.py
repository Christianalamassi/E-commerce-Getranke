from django.urls import path
from . import views


urlpatterns = [
    path('', views.basket, name="basket"),
    path('add/<basket_id>/', views.add_basket, name='add_basket'),
    path('adjust/<basket_id>/', views.fix_basket, name='fix_basket'),
    path('remove/<basket_id>/', views.remove, name='remove'),
]
