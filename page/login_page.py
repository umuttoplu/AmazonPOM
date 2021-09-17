from selenium.webdriver.common.by import By
from base.base_page import BaseClass


class LoginPage:
    """
    Website login page to user logged in.
    """
    EMAIL_TEXT = (By.ID, "ap_email")
    EMAIL_CONTINUE = (By.ID, "continue")
    PASSWORD_TEXT = (By.CLASS_NAME, "auth-required-field")
    LOGIN_BUTTON = (By.CLASS_NAME, "a-button-primary")
    CREATE_AMAZON = (By.ID, "createAccountSubmit")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)
        self.check()

    def check(self):
        (self.methods.wait_element_visible(self.CREATE_AMAZON), 'No "Create your Amazon account" button on the page!')
        (self.methods.wait_element_visible(self.EMAIL_TEXT), 'No "Email text" button on the page!')
        (self.methods.wait_element_visible(self.EMAIL_CONTINUE), 'No "Continue" button on the page!')

    def sign_in(self, email, password):
        """
        Login credentials
        """
        self.methods.wait_element_clickable(self.EMAIL_TEXT).send_keys(email)
        self.methods.wait_element_clickable(self.EMAIL_CONTINUE).click()
        self.methods.wait_element_clickable(self.PASSWORD_TEXT).send_keys(password)
        self.methods.wait_element_clickable(self.LOGIN_BUTTON).click()
