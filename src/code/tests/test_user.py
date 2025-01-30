import unittest
from src.models.user import User
from src.utils.database import Database
from src.code.utils.auth import hash_password, verify_password

class TestUserModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database(":memory:")  # Use in-memory database for testing
        cls.db._create_tables()

    def setUp(self):
        self.db = self.__class__.db
        self.db._execute_query("DELETE FROM users")  # Clear users table before each test

    def test_create_user(self):
        user_id = self.db.create_user("testuser", "test@example.com", hash_password("password"), "admin")
        self.assertIsNotNone(user_id)
        user = self.db.get_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "testuser")
        self.assertEqual(user["email"], "test@example.com")
        self.assertEqual(user["role"], "admin")
        self.assertTrue(verify_password("password", user["password_hash"]))

    def test_get_user(self):
        user_id = self.db.create_user("testuser", "test@example.com", hash_password("password"), "admin")
        user = self.db.get_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "testuser")
        self.assertEqual(user["email"], "test@example.com")
        self.assertEqual(user["role"], "admin")
        self.assertTrue(verify_password("password", user["password_hash"]))

    def test_update_user(self):
        user_id = self.db.create_user("testuser", "test@example.com", hash_password("password"), "admin")
        success = self.db.update_user(user_id, username="updateduser", email="updated@example.com", role="user")
        self.assertTrue(success)
        user = self.db.get_user(user_id)
        self.assertEqual(user["username"], "updateduser")
        self.assertEqual(user["email"], "updated@example.com")
        self.assertEqual(user["role"], "user")

    def test_delete_user(self):
        user_id = self.db.create_user("testuser", "test@example.com", hash_password("password"), "admin")
        success = self.db.delete_user(user_id)
        self.assertTrue(success)
        user = self.db.get_user(user_id)
        self.assertIsNone(user)

    def test_list_users(self):
        user_id1 = self.db.create_user("testuser1", "test1@example.com", hash_password("password1"), "admin")
        user_id2 = self.db.create_user("testuser2", "test2@example.com", hash_password("password2"), "user")
        users = self.db.list_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]["username"], "testuser1")
        self.assertEqual(users[1]["username"], "testuser2")

if __name__ == "__main__":
    unittest.main()
