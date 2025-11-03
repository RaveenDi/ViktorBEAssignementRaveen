from collections import Counter, defaultdict
from typing import List, Dict, Tuple

from part1_store_cart_model.store.cart import ShoppingCart


def recommend_next_product(carts: List[ShoppingCart]) -> Dict[str, Tuple[str, int]]:
    transition_counts = defaultdict(Counter)

    for cart in carts:
        products = cart.list_items()
        for i in range(1, len(products)):
            prev_id = str(products[i - 1].id)
            curr_id = str(products[i].id)
            transition_counts[curr_id][prev_id] += 1

    result = {}
    for product_id, counter in transition_counts.items():
        most_common_prev, count = counter.most_common(1)[0]
        result[product_id] = (most_common_prev, count)

    return result
