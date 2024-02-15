from rest_framework import serializers

class DeliveryCostRequestSerializer(serializers.Serializer):
    zone = serializers.CharField()
    organization_id = serializers.CharField()
    total_distance = serializers.FloatField()
    item_type = serializers.ChoiceField(choices=['perishable', 'non-perishable'])

class DeliveryCostResponseSerializer(serializers.Serializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)