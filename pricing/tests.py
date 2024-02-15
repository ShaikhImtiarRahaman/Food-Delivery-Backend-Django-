from django.test import TestCase
from .models import Pricing, Organization, Item
from .services import calculate_delivery_cost

class PricingTestCase(TestCase):
    def setUp(self):
        self.organization = Organization.objects.create(name="Org1")
        self.item = Item.objects.create(type="perishable", description="Food")
        self.pricing = Pricing.objects.create(
            organization=self.organization,
            item=self.item,
            zone="central",
            base_distance_in_km=5,
            km_price=1.5,
            fix_price=10
        )

    def test_calculate_delivery_cost(self):
        total_price = calculate_delivery_cost(
            organization_id=self.organization.id,
            zone="central",
            total_distance=10,
            item_type="perishable"
        )
        self.assertEqual(total_price, 20.0)