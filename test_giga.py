# def test_prosto(page: Page):
#     page.goto("http://erp-new.karman24.ru/login")
#     # page.get_by_role("textbox", name="Email").click()
#     page.get_by_role("textbox", name="Email").fill("test1@karman24.ru")
#     # page.get_by_role("textbox", name="Пароль").click()
#     page.get_by_role("textbox", name="Пароль").fill("Qwerty123456")
#     page.get_by_role("button", name="Войти").click()
#     page.get_by_role("link", name="👥 Клиенты").click()
#     page.get_by_role("button", name="Добавить клиента").click()
#     page.get_by_role("button", name="Добавить контакт").click()
#     page.get_by_role("textbox", name="Значение").fill("+7 (939) 222-22-22")
#     page.get_by_role("button", name="Готово").click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_prosto():
    driver = webdriver.Chrome()  # Убедись, что у тебя установлен ChromeDriver
    try:
        driver.get("http://erp-new.karman24.ru/login")

        # Ввод email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="Email"]'))
        )
        email_input.send_keys("test1@karman24.ru")

        # Ввод пароля
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="Пароль"]'))
        )
        password_input.send_keys("Qwerty123456")

        # Нажатие на кнопку "Войти"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Войти"]'))
        )
        login_button.click()

        # Переход к разделу "Клиенты"
        clients_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="👥 Клиенты"]'))
        )
        clients_link.click()

        # Нажатие на кнопку "Добавить клиента"
        add_client_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Добавить клиента"]'))
        )
        add_client_button.click()

        # Нажатие на кнопку "Добавить контакт"
        add_contact_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Добавить контакт"]'))
        )
        add_contact_button.click()

        # Ввод значения в поле "Значение"
        value_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="Значение"]'))
        )
        value_input.send_keys("+7 (939) 222-22-22")

        # Нажатие на кнопку "Готово"
        ready_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Готово"]'))
        )
        ready_button.click()

    finally:
        driver.quit()

if __name__ == "__main__":
    test_prosto()

