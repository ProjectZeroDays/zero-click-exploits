import logging
from src.utils.database import Database
from src.code.controllers.user_controller import UserController
from src.code.controllers.product_controller import ProductController

def main():
    logging.basicConfig(level=logging.INFO)
    db = Database()

    user_controller = UserController(db)
    product_controller = ProductController(db)

    # Example usage
    new_user_id = user_controller.create_user("testuser", "test@example.com", "hashed_password", "admin")
    if new_user_id:
        retrieved_user = user_controller.get_user(new_user_id)
        if retrieved_user:
            logging.info(f"Retrieved user: {retrieved_user}")
            user_controller.update_user(retrieved_user["user_id"], username="updated_user")
            updated_user = user_controller.get_user(new_user_id)
            if updated_user:
                logging.info(f"Updated user: {updated_user}")
                user_controller.delete_user(updated_user["user_id"])
                logging.info("User deleted.")
            else:
                logging.error("Failed to update user.")
        else:
            logging.error("Failed to retrieve user.")
    else:
        logging.error("Failed to create user.")
    all_users = user_controller.list_users()
    logging.info(f"All users: {all_users}")

    new_product_id = product_controller.create_product("Test Product", "This is a test product.", 19.99, 100)
    if new_product_id:
        retrieved_product = product_controller.get_product(new_product_id)
        if retrieved_product:
            logging.info(f"Retrieved product: {retrieved_product}")
            product_controller.update_product(retrieved_product["product_id"], price=24.99)
            updated_product = product_controller.get_product(new_product_id)
            if updated_product:
                logging.info(f"Updated product: {updated_product}")
                product_controller.delete_product(updated_product["product_id"])
                logging.info("Product deleted.")
            else:
                logging.error("Failed to update product.")
        else:
            logging.error("Failed to retrieve product.")
    else:
        logging.error("Failed to create product.")
    all_products = product_controller.list_products()
    logging.info(f"All products: {all_products}")

if __name__ == "__main__":
    main()
