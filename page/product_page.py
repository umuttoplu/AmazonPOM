from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from page.wishlist_page import WishlistPage


class ProductPage:
    """
    Product page to add list

    """
    ADD_TO_LIST = (By.ID, "add-to-wishlist-button-group")
    ADD_TO_LIST_UNAVAILABLE = (By.ID, "add-to-wishlist-button-submit")
    VIEW_YOUR_LIST = (By.ID, "WLHUC_viewlist")
    TITLE = (By.ID, "titleSection")
    PRODUCT_CONTROL = (By.XPATH, "//h3[@class='a-size-base']")
    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def product_add_list(self):
        """
        Adds product to the add list

        """
        title = self.methods.wait_element_clickable(self.TITLE).text
        if self.methods.selector_exists(self.ADD_TO_LIST):
            self.methods.wait_element_clickable(self.ADD_TO_LIST).click()
        else:
            self.methods.wait_element_clickable(self.ADD_TO_LIST_UNAVAILABLE).click()
        self.methods.wait_element_clickable(self.VIEW_YOUR_LIST).click()
        name = self.methods.wait_all_element(self.PRODUCT_CONTROL)[0].text
        assert title == name, "Not the correct product added to wishlist"
        return WishlistPage(self.driver)
