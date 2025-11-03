from typing import List
from uuid import UUID

from store.models import Product


class ShoppingCart:
    def __init__(self) -> None:
        self._items: List[Product] = []

    def add_product(self, product: Product) -> None:
        self._items.append(product)

    def remove_product_by_id(self, product_id: UUID) -> bool:
        for i, item in enumerate(self._items):
            if item.id == product_id:
                del self._items[i]
                return True
        return False

    def total_price(self) -> float:
        return sum(item.price_eur for item in self._items)

    def total_weight(self) -> float:
        return sum(item.get_weight_kg() for item in self._items)

    def list_items(self) -> List[Product]:
        return self._items.copy()