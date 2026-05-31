from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Компонент формы логина
        self.login_form = LoginFormComponent(page)
        # Локатор для алерта
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")