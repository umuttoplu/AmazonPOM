from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from page.product_page import ProductPage


class CategoryPage:
    """
    Amazon selects products from the category page

    """
    PAGE_CONTROL = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    SECOND_PAGE_CONTROL = (By.XPATH, "//img[@data-image-index='17']")
    GO_TO_SECOND_PAGE = (By.CLASS_NAME, "a-normal")
    THIRD_PRODUCT = (By.XPATH, "//img[@data-image-index='19']")
    PRODUCT_LIST = (By.CLASS_NAME, "s-main-slot")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.PRODUCT_LIST), 'Could not found any product!')

    def select_product(self, search):
        """"
        The second page goes through and selects the third product

        """
        self.methods.wait_element_clickable(self.GO_TO_SECOND_PAGE).click()
        assert self.methods.wait_element_visible(self.SECOND_PAGE_CONTROL), "Not in the second page"
        assert self.methods.wait_element_visible(self.PAGE_CONTROL).text == '"samsung"', \
            "Not in the search page."
        self.methods.wait_element_visible(self.THIRD_PRODUCT).click()
        return ProductPage(self.driver)
