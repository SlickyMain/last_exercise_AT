import time
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize("link", ["1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    good_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, good_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_thing_in_basket()
    page.check_amount_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_to_login()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_to_basket_from_header()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_clean()
    basket_page.message_about_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, reg)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "qwertyASD123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        good_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, good_link)
        page.open()
        page.add_to_basket()
        page.check_thing_in_basket()
        page.check_amount_in_basket()
