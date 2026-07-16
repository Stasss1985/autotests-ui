from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
import allure


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(page,'registration-form-email-input', "email_registration_input")
        self.username_input = Input(page,'registration-form-username-input', "username_registration_input")
        self.password_input = Input(page,'registration-form-password-input', "password_registration_input")
        self.submit_button = Button(page,'registration-page-registration-button', "submit_button")

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str) -> None:
        self.email_input.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()
        self.submit_button.check_visible()
        self.email_input.check_have_value(email)
        self.username_input.check_have_value(username)
        self.password_input.check_have_value(password)