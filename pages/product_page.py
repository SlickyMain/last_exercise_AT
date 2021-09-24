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
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK).text, "No success message after adding"

    def check_amount_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text in self.browser.find_element(*ProductPageLocators.AMOUNT).text

