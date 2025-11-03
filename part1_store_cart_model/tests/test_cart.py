import unittest
from uuid import UUID

from part1_store_cart_model.store.analytics.recommender import recommend_next_product
from part1_store_cart_model.store.cart import ShoppingCart
from part1_store_cart_model.store.models import Book, MusicAlbum, SoftwareLicense


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.book = Book(title="1984", author="Orwell", num_pages=328, weight_kg=0.5, price_eur=12.0)
        self.album = MusicAlbum(artist="Pink Floyd", title="The Wall", num_tracks=10, weight_kg=0.2, price_eur=15.0)
        self.license = SoftwareLicense(name="Photoshop", price_eur=25.0)

    def test_add_product(self):
        self.cart.add_product(self.book)
        self.assertEqual(len(self.cart.list_items()), 1)

    def test_remove_product_by_id_success(self):
        self.cart.add_product(self.album)
        result = self.cart.remove_product_by_id(self.album.id)
        self.assertTrue(result)
        self.assertEqual(len(self.cart.list_items()), 0)

    def test_remove_product_by_id_failure(self):
        fake_id = UUID("12345678-1234-5678-1234-567812345678")
        result = self.cart.remove_product_by_id(fake_id)
        self.assertFalse(result)

    def test_total_price(self):
        self.cart.add_product(self.book)
        self.cart.add_product(self.album)
        self.assertEqual(self.cart.total_price(), 27.0)

    def test_total_weight(self):
        self.cart.add_product(self.book)
        self.cart.add_product(self.album)
        self.cart.add_product(self.license)
        self.assertAlmostEqual(self.cart.total_weight(), 0.7)

    def test_unique_ids(self):
        book2 = Book(title="Animal Farm", author="Orwell", num_pages=120, weight_kg=0.3, price_eur=10.0)
        self.assertNotEqual(self.book.id, book2.id)

    def test_recommendation_engine_basic(self):
        # Create multiple carts to simulate user behavior
        cart1 = ShoppingCart()
        cart1.add_product(self.book)
        cart1.add_product(self.album)

        cart2 = ShoppingCart()
        cart2.add_product(self.book)
        cart2.add_product(self.album)

        cart3 = ShoppingCart()
        cart3.add_product(self.book)
        cart3.add_product(self.license)

        cart4 = ShoppingCart()
        cart4.add_product(self.album)
        cart4.add_product(self.license)

        carts = [cart1, cart2, cart3, cart4]

        recommendations = recommend_next_product(carts)

        self.assertEqual(recommendations[str(self.album.id)], (str(self.book.id), 2))
        self.assertEqual(recommendations[str(self.license.id)], (str(self.book.id), 1))

if __name__ == '__main__':
    unittest.main()
