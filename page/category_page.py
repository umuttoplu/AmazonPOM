from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from page.product_page import ProductPage


class CategoryPage:
    """
    Amazon selects products from the category page

    """
    PAGE_CONTROL = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    GO_TO_SECOND_PAGE = (By.CLASS_NAME, "a-normal")
    GO_TO_SECOND_PAGE_ALTERNATIVE = (By.CLASS_NAME, "s-pagination-button")
    THIRD_PRODUCT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".s-main-slot.s-result-list.s-search-results")

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

        if self.methods.selector_exists(self.GO_TO_SECOND_PAGE):
            self.methods.wait_all_element(self.GO_TO_SECOND_PAGE)[0].click()
        else:
            self.methods.wait_all_element(self.GO_TO_SECOND_PAGE_ALTERNATIVE)[0].click()

        current_url = self.driver.current_url
        second_page_control = "page=2"
        assert second_page_control in current_url, "Not in the second page."
        page_control = self.methods.wait_element_visible(self.PAGE_CONTROL).text
        assert page_control == search, "Search results are not for 'samsung'"
        self.methods.wait_all_element(self.THIRD_PRODUCT)[2].click()
        return ProductPage(self.driver)
