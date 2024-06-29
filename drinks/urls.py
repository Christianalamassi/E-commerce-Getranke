from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_drink, name='drinks'),
    path('<drink_id>', views.each_drink, name="each_drink")
]