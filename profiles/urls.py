from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name ='profile'),
    path(
        'order_details/<order_number>', views.order_details, name='order_details'
        )
]
