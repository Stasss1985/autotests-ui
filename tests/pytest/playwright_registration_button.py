from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим кнопку "Registration" и проверяем что она disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Находим поле "Email" и заполняем его
    email_fild = page.get_by_test_id('registration-form-email-input').locator('input')
    email_fild.fill("user.name@gmail.com")

    # Находим поле "username" и заполняем его
    username_fild = page.get_by_test_id('registration-form-username-input').locator('input')
    username_fild.fill("username")

    # Находим поле "Password" и заполняем его
    password_fill = page.get_by_test_id('registration-form-password-input').locator('input')
    password_fill.fill("password")

    # Находим кнопку "Registration" и проверяем что она enabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()




    page.wait_for_timeout(4000)