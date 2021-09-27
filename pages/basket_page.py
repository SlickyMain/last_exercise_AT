from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def basket_is_clean(self):
        assert self.is_not_element_present(By.CLASS_NAME, "basket_summary")

    def message_about_empty_basket(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
            "en-US": "Your basket is empty."
        }
        message = self.browser.find_element(By.TAG_NAME, "p").text
        current_language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert languages[current_language] in message, "Basket not empty or no message"
