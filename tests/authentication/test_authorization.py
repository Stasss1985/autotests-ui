import pytest
import allure

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION)  # Добавили feature
@allure.story(AllureStory.AUTHORIZATION)  # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
@allure.severity(Severity.CRITICAL)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title("Авторизация с не верным паспортом или паролем")
    @allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
    @allure.step("Авторизация с не верным паспортом или паролем")
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        #with allure.step("Открытие страницы"):
            login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        #with allure.step("Ввод емейла и паспорта"):
            login_page.login_form.fill(email=email, password=password)
        #with allure.step("Клик по кнопки Войти"):
            login_page.click_login_button()
        #with allure.step("Проверка предупреждения"):
            login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("Успешная авторизация")
    @allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
    @allure.step("Успешная авторизация")
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @allure.title("Не успешная регистрация с не верным email, username и password")
    @allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")
