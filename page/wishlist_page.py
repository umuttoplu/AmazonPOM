from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class WishlistPage:
    """


    """
    DELETE_ITEM = (By.NAME, "submit.deleteItem")
    DELETED = (By.XPATH, ".//*[contains(text(),'Deleted')]")

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
        self.methods.wait_all_element(WishlistPage.DELETE_ITEM)[0].click()
        assert self.methods.selector_exists(WishlistPage.DELETED), "Did not delete the product."
