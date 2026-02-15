from playwright.sync_api import sync_playwright, Page, Playwright
import pytest


@pytest.fixture()
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
