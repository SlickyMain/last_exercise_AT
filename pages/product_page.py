from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        assert ec.element_to_be_clickable(self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)), "Button\
                                                                                                    not available"
        add_button.click()

    def check_thing_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK).text, "No success message after adding"

    def check_amount_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text in self.browser.find_element(*ProductPageLocators.AMOUNT).text, "Wrong amount in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK), \
            "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK), \
            "Message don't disappear"

    def guest_to_login(self):
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "There is no login page"
