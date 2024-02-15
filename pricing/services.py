from .models import Pricing

def calculate_delivery_cost(organization_id, zone, total_distance, item_type):
    pricing = Pricing.objects.filter(
        organization_id=organization_id,
        zone=zone,
        item__type=item_type
    ).first()
    if not pricing:
        return None
    base_price = pricing.fix_price
    if total_distance > pricing.base_distance_in_km:
        additional_distance = total_distance - pricing.base_distance_in_km
        base_price += additional_distance * pricing.km_price
    return base_price