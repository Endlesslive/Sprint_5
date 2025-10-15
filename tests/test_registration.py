import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators
from helpers.generators import generate_email, generate_password, generate_name


class TestRegistration:
    """Тесты регистрации пользователя"""
    
    def test_successful_registration(self, driver, base_url):
        """Тест успешной регистрации с корректными данными"""
        driver.get(base_url)
        login_button = WebDriverWait(driver, 10).until(                             # Клик по кнопке "Войти в аккаунт"
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
        register_link = WebDriverWait(driver, 10).until(                            # Переход на страницу регистрации
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        register_link.click()
        name_input = WebDriverWait(driver, 10).until(                                # Заполнение формы регистрации
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
        name_input.send_keys(generate_name())
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(generate_email())
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(generate_password(8))
        register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON) # Клик по кнопке "Зарегистрироваться"
        register_button.click()
        login_title = WebDriverWait(driver, 10).until(                               # Проверка перехода на страницу входа
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert login_title.is_displayed()
    
    def test_registration_with_incorrect_password(self, driver, base_url):
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        driver.get(base_url)
        login_button = WebDriverWait(driver, 10).until(                            # Клик по кнопке "Войти в аккаунт"
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
        register_link = WebDriverWait(driver, 10).until(                          # Переход на страницу регистрации
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK))
        register_link.click()
        name_input = WebDriverWait(driver, 10).until(                                  # Заполнение формы с коротким паролем
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
        name_input.send_keys(generate_name())
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(generate_email())
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys("12345")  # Пароль менее 6 символов
        register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)  # Клик по кнопке "Зарегистрироваться"
        register_button.click()
        error_message = WebDriverWait(driver, 10).until(                                  # Проверка отображения ошибки
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert error_message.is_displayed()
