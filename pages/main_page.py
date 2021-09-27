from pages.base_page import BasePage
from pages.locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def guest_going_to_basket_from_header(self):
        self.go_to_basket_from_header(*BasePageLocators.HEADER_BUTTON_BASKET)
        assert "basket" in self.browser.current_url


