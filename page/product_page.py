from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from page.wishlist_page import WishlistPage


class ProductPage:
    """
    Product page to add list

    """
    ADD_TO_LIST = (By.ID, "add-to-wishlist-button-group")
    ADD_TO_LIST_UNAVAILABLE = (By.ID, "add-to-wishlist-button-submit")
    VIEW_YOUR_LIST = (By.XPATH, "//a[contains(text(), 'View Your List')]")
    TITLE = (By.ID, "titleSection")
    ADDED_PRODUCT_TITLE = (By.CLASS_NAME, "huc-atwl-header-small")
    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def add_product_to_wishlist(self):
        """
        Adds product to the add list

        """
        if self.methods.is_element_visible(self.ADD_TO_LIST):
            self.methods.wait_element_clickable(self.ADD_TO_LIST).click()
        else:
            self.methods.wait_element_clickable(self.ADD_TO_LIST_UNAVAILABLE).click()

    def get_product_title(self):
        """
        Returns selected product's title

        """
        title = self.methods.wait_element_clickable(self.TITLE).text
        return title

    def get_added_product_title(self):
        """
        Returns True if correct product added to withlist, False if not

        """
        added_product_title = self.methods.wait_element_visible(self.ADDED_PRODUCT_TITLE).text
        return added_product_title

    def click_view_your_list(self):
        """
        Clicks to 'View Your List' button from opened modal

        """
        self.methods.wait_element_clickable(self.VIEW_YOUR_LIST).click()
        return WishlistPage(self.driver)
