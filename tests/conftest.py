from playwright.sync_api import sync_playwright, Page, Playwright, expect
import pytest


@pytest.fixture(scope='session')
def chromium_page(playwright: Playwright) -> Page:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Открываем новую страницу в рамках контекста
    yield browser.new_page()
    # Закрываем браузер после выполнения тестов
    browser.close()


#     Первый старый вариант
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         # Запускаем Chromium браузер в обычном режиме (не headless)
#         browser = playwright.chromium.launch(headless=False)
#         # Открываем новую страницу в рамках контекста
#         yield browser.new_page()
#         # Закрываем браузер после выполнения тестов
#         browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    chromium_page.context.storage_state(path="browser-state.json")


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Реализация логики работы фикстуры
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    yield page
    browser.close()
