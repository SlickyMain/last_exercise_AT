from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_ABOUT_BOOK = (By.CLASS_NAME, "alertinner")
    PRICE = (By.CLASS_NAME, "price_color")
    AMOUNT = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
