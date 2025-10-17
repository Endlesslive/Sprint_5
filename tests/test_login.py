import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import (
    MainPageLocators, 
    LoginPageLocators, 
    RegistrationPageLocators,
    PasswordRecoveryPageLocators
)
from constants import BASE_URL

class TestLogin:
    """Тесты входа в систему"""
    def test_login_via_main_page_button(self, driver, register_user, login_user):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver.get(BASE_URL)
        # Клик по кнопке "Войти в аккаунт"
        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
        # Используем фикстуру для входа
        login_user(register_user['email'], register_user['password'])
        # Проверка успешного входа
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        assert personal_account_button.is_displayed(), "Кнопка личного кабинета не отображается"
    
    def test_login_via_personal_account_button(self, driver, register_user, login_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get(BASE_URL)
        # Клик по кнопке "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        # Ждем загрузки формы входа
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        # Используем фикстуру для входа
        login_user(register_user['email'], register_user['password'])
        # Проверка успешного входа
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        assert personal_account_button.is_displayed(), "Кнопка личного кабинета не отображается"
    
    def test_login_via_registration_form(self, driver, register_user, login_user):
        """Тест входа через кнопку в форме регистрации"""
        driver.get(f"{BASE_URL}register")
        # Клик по ссылке "Войти"
        login_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK))
        login_link.click()
        # Ждем загрузки формы входа
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        # Используем фикстуру для входа
        login_user(register_user['email'], register_user['password'])
        # Проверка успешного входа
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        assert personal_account_button.is_displayed(), "Кнопка личного кабинета не отображается"
    
    def test_login_via_password_recovery_form(self, driver, register_user, login_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        driver.get(f"{BASE_URL}forgot-password")
        # Клик по ссылке "Войти"
        login_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(PasswordRecoveryPageLocators.LOGIN_LINK))
        login_link.click()
        # Ждем загрузки формы входа
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        # Используем фикстуру для входа
        login_user(register_user['email'], register_user['password'])
        # Проверка успешного входа
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        assert personal_account_button.is_displayed(), "Кнопка личного кабинета не отображается"