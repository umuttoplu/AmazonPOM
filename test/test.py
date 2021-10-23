import unittest
from selenium import webdriver
from base.base_page import BaseClass
from page.main_page import HomePage


class AmazonTest(unittest.TestCase):
    """Test case is:
    1. go http://www.amazon.com and confirm
    2. open the login page and log-in with your account
    3. type 'samsung' to the search box and click to the search button
    4. confirm that there are results for 'samsung'
    5. go second page of the search page and confirm that it is the second page
    6. click on the third product of the top and click 'Add to List' button
    7. click on the "View Your List" where is the top of the page
    8. confirm that the same product is added from previous page
    9. delete this product from wishlist page by clicking 'Delete item' button
    10. confirm that this product no longer on the wishlist
    """

    def setUp(self):
        """
        Selenium initializing requirements

        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.method = BaseClass(self.driver)
        self.amazon_main = HomePage(self.driver)

    def test_amazon(self):
        self.login_page = self.amazon_main.sign_in_button_click()
        self.login_page.sign_in("umuttoplu00@hotmail.com", "testautomation2021")
        self.category_page = self.amazon_main.search_query("samsung")
        self.product_page = self.category_page.select_product('"samsung"')
        self.wishlist_page = self.product_page.product_add_list()
        self.wishlist_page.delete_product()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
