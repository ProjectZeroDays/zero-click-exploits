import unittest
from src.models.product import Product
from src.utils.database import Database

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database(":memory:")  # Use in-memory database for testing
        cls.db._create_tables()

    def setUp(self):
        self.db = self.__class__.db
        self.db._execute_query("DELETE FROM products")  # Clear products table before each test

    def test_create_product(self):
        product_id = self.db.create_product("Test Product", "This is a test product.", 19.99, 100)
        self.assertIsNotNone(product_id)
        product = self.db.get_product(product_id)
        self.assertIsNotNone(product)
        self.assertEqual(product["name"], "Test Product")
        self.assertEqual(product["description"], "This is a test product.")
        self.assertEqual(product["price"], 19.99)
        self.assertEqual(product["stock"], 100)

    def test_get_product(self):
        product_id = self.db.create_product("Test Product", "This is a test product.", 19.99, 100)
        product = self.db.get_product(product_id)
        self.assertIsNotNone(product)
        self.assertEqual(product["name"], "Test Product")
        self.assertEqual(product["description"], "This is a test product.")
        self.assertEqual(product["price"], 19.99)
        self.assertEqual(product["stock"], 100)

    def test_update_product(self):
        product_id = self.db.create_product("Test Product", "This is a test product.", 19.99, 100)
        success = self.db.update_product(product_id, name="Updated Product", description="Updated description", price=24.99, stock=50)
        self.assertTrue(success)
        product = self.db.get_product(product_id)
        self.assertEqual(product["name"], "Updated Product")
        self.assertEqual(product["description"], "Updated description")
        self.assertEqual(product["price"], 24.99)
        self.assertEqual(product["stock"], 50)

    def test_delete_product(self):
        product_id = self.db.create_product("Test Product", "This is a test product.", 19.99, 100)
        success = self.db.delete_product(product_id)
        self.assertTrue(success)
        product = self.db.get_product(product_id)
        self.assertIsNone(product)

    def test_list_products(self):
        product_id1 = self.db.create_product("Test Product 1", "This is a test product 1.", 19.99, 100)
        product_id2 = self.db.create_product("Test Product 2", "This is a test product 2.", 29.99, 200)
        products = self.db.list_products()
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0]["name"], "Test Product 1")
        self.assertEqual(products[1]["name"], "Test Product 2")

if __name__ == "__main__":
    unittest.main()
