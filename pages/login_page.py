from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        try:
            email_field.send_keys(email)
            password_field.send_keys(password)
            confirm_password_field.send_keys(password)
            submit_button.click()
        except NoSuchElementException:
            print("Elements wasn't found")
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESS_MESSAGE), "User is not registered"

    def should_be_login_url(self):
        correct_url = self.browser.current_url
        assert "login" in correct_url, "URL does not contain 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No Login Form found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "No registration Form found"
