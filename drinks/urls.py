from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_drink, name='drinks'),
    path('<int:drink_id>/', views.each_drink, name="each_drink"),
    path('add_drink/', views.add_drink, name="add_drink"),
    path('edit_drink/<int:drink_id>/', views.edit_drink, name="edit_drink"),
    path(
        'delete_drink/<int:drink_id>/', views.delete_drink, name="delete_drink"
        )
]
