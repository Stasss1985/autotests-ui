import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page, 'login-form-email-input', "email_input")
        self.password_input = Input(page,'login-form-password-input', "password_input")
        self.submit_button = Button(page,'login-page-login-button', "submit_login_button")

    @allure.step("Fill login form")
    def fill(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step("Check visible login form")
    def check_visible(self, email: str, password: str) -> None:
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.submit_button.check_visible()
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)