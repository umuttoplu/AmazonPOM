from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BaseClass(object):
    """
    Base class to initialize the base page that will be called from all pages

    """
    def __init__(self, driver, base_url='http://www.amazon.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def wait(self):
        """
        Driver to use implicitly time

        """
        return WebDriverWait(self.driver, 30)

    def wait_element_clickable(self, element):
        """
        Wait for element to present
        :param element: locator of the element to find

        """
        return self.wait().until(ec.element_to_be_clickable(element))

    def wait_all_elements(self, element):
        """
        Wait for element to present
        :param element: locator of the element to find

        """
        return self.wait().until(ec.presence_of_all_elements_located(element))

    def wait_element_visible(self, element):
        """
        Wait for element to visible

        """
        return self.wait().until(ec.visibility_of_element_located(element))

    def selector_exists(self, element):
        """
        Selector exists for assert

        """
        try:
            return self.wait_element_clickable(element)
        except TimeoutException:
            return False
