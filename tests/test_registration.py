from playwright.sync_api import sync_playwright, Page


def test_successful_registration(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    # context.storage_state(path="browser-state.json")

# Остальной код регистрации нового пользователя без изменений
