from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Пытаемся проверить, что несуществующий локатор виден на странице
    unknown = page.locator('#unknown')
    expect(unknown).to_be_visible()


'''
2. Некорректное взаимодействие с элементом
Такое происходит, если, например, вы пытаетесь ввести текст в кнопку.

Пример:
Добавим скрипт, который вводит текст в кнопку "Login".

В файле playwright_errors.py добавим:

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Пытаемся ввести текст в кнопку Login
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.fill('unknown')
'''

'''
3. Работа с элементом до его появления в DOM-дереве
Часто это связано с динамическим рендерингом страниц. Например, вы пытаетесь выполнить JavaScript-код на элементе, который еще не загружен.

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')
    
    # Пытаемся изменить текст заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

                  
При запуске скрипта возникнет ошибка:

playwright._impl._errors.Error: Page.evaluate: TypeError: Cannot set properties of null (setting 'textContent')
    at eval (eval at evaluate (:234:30), <anonymous>:2:23)
    at eval (<anonymous>)
    at UtilityScript.evaluate (<anonymous>:234:30)
    at UtilityScript.<anonymous> (<anonymous>:1:44)

                  
Анализ ошибки:
TypeError: Cannot set properties of null: элемент не найден, так как не успел загрузиться.
Такое случается в динамических приложениях (SPA), где элементы появляются только после завершения сетевых запросов или выполнения JS-скриптов.
Решение:
Добавьте явное ожидание загрузки страницы. Например:

page.goto(
    "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
    wait_until='networkidle'  # Ждем завершения сетевых запросов
)

                  
Параметр wait_until='networkidle' гарантирует, что страница полностью загрузилась, и элементы DOM стали доступны.'''