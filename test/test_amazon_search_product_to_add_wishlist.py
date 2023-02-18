import unittest
from selenium import webdriver
from base.base_page import BaseClass
from page.main_page import HomePage
from webdriver_manager.chrome import ChromeDriverManager


class AmazonTest(unittest.TestCase):
    """ Test case is:

        1. Open the login page and log-in with your account
        2. Type 'samsung' to the search box and click to the search button
        3. Confirm that there are results for searched keyword 'samsung'
        4. Go to second page of the search page and confirm that it is the second page
        5. Click to given product index and click 'Add to List' button
        6. Click on the "View Your List" from opened modal
        7. Confirm that the same product is added from previous page
        9. Delete added product from wishlist page by clicking 'Delete item' button

    """
    search_keyword = "samsung"
    email = ""
    password = ""

    def setUp(self):
        """
        Selenium initializing requirements

        """
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.method = BaseClass(self.driver)

    def test_amazon_search_product_to_add_wishlist(self):

        amazon_main = HomePage(self.driver)
        login_page = amazon_main.sign_in_button_click()
        login_page.sign_in(self.email, self.password)

        category_page = amazon_main.search_query(self.search_keyword)
        self.assertEqual(category_page.get_searched_keyword(), self.search_keyword, "Searched keyword does not match!")

        category_page.click_next_page_button()
        self.assertEqual(category_page.get_current_page_number(), '2', "Current page number does not match!")

        product_page = category_page.select_product(5)
        product_page.add_product_to_wishlist()

        product_title = product_page.get_product_title()
        self.assertEqual(product_title, product_page.get_added_product_title(),
                         "Selected and added product titles are not same!")
        wishlist_page = product_page.click_view_your_list()

        wishlist_page.delete_product_from_wishlist()
        self.assertTrue(wishlist_page.is_product_deleted(), "Product could not deleted from wishlist!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
