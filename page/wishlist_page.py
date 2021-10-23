from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class WishlistPage:
    """
    Delete added product from wishlist

    """
    DELETE_ITEM = (By.NAME, "submit.deleteItem")
    DELETED = (By.CLASS_NAME, "a-alert-inline-success")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.DELETE_ITEM), 'No "Delete" button on the page!')

    def delete_product(self):
        """
        Delete product to the wish list
        """
        self.methods.wait_element_clickable(WishlistPage.DELETE_ITEM).click()
        assert self.methods.selector_exists(WishlistPage.DELETED), "Did not delete the product."
