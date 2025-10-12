import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.page_locators import (
    MainPageLocators, 
    LoginPageLocators, 
    RegistrationPageLocators,
    PersonalAccountPageLocators
)
from helpers.generators import generate_email, generate_password, generate_name


class TestLogout:
    """Тесты выхода из системы"""
    
    @pytest.fixture(autouse=True)
    def setup_and_login(self, driver, base_url):
        """Создание и вход пользователя перед каждым тестом"""
        self.test_email = generate_email()
        self.test_password = generate_password(8)
        self.test_name = generate_name()
        
        # Регистрация
        driver.get(f"{base_url}register")
        
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        name_input.send_keys(self.test_name)
        
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(self.test_email)
        
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(self.test_password)
        
        register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()
        
        # Небольшая пауза после клика
        time.sleep(2)
        
        # Вход сразу после регистрации
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(self.test_email)
        
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(self.test_password)
        
        time.sleep(1)
        
        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        )
        login_submit_button.click()
        
        # Ожидание успешного входа
        time.sleep(3)
        
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
            )
        except TimeoutException:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            )
    
    def test_logout_from_personal_account(self, driver, base_url):
        """Тест выхода из аккаунта через личный кабинет"""
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        # Ожидание загрузки страницы личного кабинета
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE)
        )
        
        time.sleep(1)
        
        # Клик по кнопке "Выход"
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        # Проверка перехода на страницу входа
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
