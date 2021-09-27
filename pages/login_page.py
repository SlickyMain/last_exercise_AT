from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from mimesis import Person


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        mail.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2)
        password2.send_keys(password)
        sub = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        sub.click()
