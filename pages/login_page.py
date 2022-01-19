from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "This is not the url of the login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_RESET), "Login reset link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration username field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1), "First registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2), "Second registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit button is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        password_2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)

        email_field.send_keys(email)
        password_1_field.send_keys(password)
        password_2_field.send_keys(password)
        registration_button.click()


