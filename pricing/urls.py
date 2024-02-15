from django.urls import path
from .views import CalculateDeliveryCost

urlpatterns = [
    path('calculate_delivery_cost/', CalculateDeliveryCost.as_view(), name='calculate_delivery_cost'),
]
