from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим поле "Email" и заполняем его
    email_fild = page.get_by_test_id('registration-form-email-input').locator('input')
    email_fild.fill("user.name@gmail.com")

    # Находим поле "username" и заполняем его
    username_fild = page.get_by_test_id('registration-form-username-input').locator('input')
    username_fild.fill("username")

    # Находим поле "Password" и заполняем его
    password_fill = page.get_by_test_id('registration-form-password-input').locator('input')
    password_fill.fill("password")

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id('registration-page-registration-button')
    page.wait_for_timeout(3000)
    registration_button.hover()
    page.wait_for_timeout(3000)
    registration_button.click()

    # После перехода ищем заголовок "Dashboard" и сравниваем текст заголовка
    dashboard_title_name = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title_name).to_be_visible()
    expect(dashboard_title_name).to_have_text('Dashboard')


    page.wait_for_timeout(4000)