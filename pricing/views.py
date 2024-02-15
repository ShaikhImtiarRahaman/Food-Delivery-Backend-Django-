from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pricing
from .services import calculate_delivery_cost
from .serializers import DeliveryCostRequestSerializer, DeliveryCostResponseSerializer

# Create your views here.


class CalculateDeliveryCost(APIView):
    def post(self, request):
        serializer = DeliveryCostRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        total_price = calculate_delivery_cost(
            organization_id=data['organization_id'],
            zone=data['zone'],
            total_distance=data['total_distance'],
            item_type=data['item_type']
        )
        response_data = {'total_price': total_price}
        response_serializer = DeliveryCostResponseSerializer(data=response_data)
        response_serializer.is_valid()
        return Response(response_serializer.data)