from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class WishlistPage:
    """
    Delete added product from wishlist

    """
    DELETE_ITEM = (By.NAME, "submit.deleteItem")
    DELETED_SUCCESSFULLY = (By.CLASS_NAME, "a-alert-inline-success")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.DELETE_ITEM), 'No "Delete" button on the page!')

    def delete_product_from_wishlist(self):
        """
        Delete product from wish list

        """
        self.methods.wait_element_clickable(self.DELETE_ITEM).click()

    def is_product_deleted(self):
        """
        Returns True if product deleted, False if not

        """
        return self.methods.is_element_visible(self.DELETED_SUCCESSFULLY)
