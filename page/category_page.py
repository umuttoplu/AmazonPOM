from selenium.webdriver.common.by import By
from base.base_page import BaseClass
from page.product_page import ProductPage


class CategoryPage:
    """
    Amazon selects products from the category page

    """
    SEARCHED_KEYWORD = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    CURRENT_PAGE_NUMBER = (By.CSS_SELECTOR, ".s-pagination-selected")
    NEXT_PAGE = (By.CSS_SELECTOR, ".s-pagination-next")
    PRODUCT = (By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
    PRODUCT_LIST = (By.CLASS_NAME, "s-main-slot")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.PRODUCT_LIST), 'Could not found any product!')

    def select_product(self, index):
        """"
        Selects product from category page
        :param int index: index of requested product

        """
        products = self.methods.wait_all_elements(self.PRODUCT)
        products[index].click()
        return ProductPage(self.driver)

    def click_next_page_button(self):
        """"
        Click Next button from pagination

        """
        self.methods.wait_element_clickable(self.NEXT_PAGE).click()

    def get_current_page_number(self):
        """"
        Returns current page number

        """
        return self.methods.wait_element_visible(self.CURRENT_PAGE_NUMBER).text

    def get_searched_keyword(self):
        """"
        Returns searched text after search applied

        """
        return self.methods.wait_element_visible(self.SEARCHED_KEYWORD).text.replace('"', "")
