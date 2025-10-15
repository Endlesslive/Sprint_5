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
    def test_logout_from_personal_account(self, driver, base_url):
        """Тест выхода из аккаунта через личный кабинет"""
        personal_account_button = WebDriverWait(driver, 10).until(                           # Переход в личный кабинет
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        WebDriverWait(driver, 10).until(                                                     # Ожидание загрузки страницы личного кабинета
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE))
        expected_conditions(1)
        logout_button = WebDriverWait(driver, 10).until(                                     # Клик по кнопке "Выход"
            EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        logout_button.click()