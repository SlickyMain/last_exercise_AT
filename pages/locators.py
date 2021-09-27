from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    HEADER_BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    BASKET_CONTAINS = (By.CSS_SELECTOR, "#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD1 = (By.NAME, "registration-password1")
    PASSWORD_FIELD2 = (By.NAME, "registration-password2")
    SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_ABOUT_BOOK = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE = (By.CLASS_NAME, "price_color")
    AMOUNT = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
