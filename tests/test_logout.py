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
from constants import BASE_URL, DEFAULT_TIMEOUT, MEDIUM_WAIT

class TestLogout:
    """Тесты выхода из системы"""
    def test_logout_from_personal_account(self, driver, authorized_user):
        personal_account_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE))
        logout_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(PersonalAccountPageLocators.LOGOUT_BUTTON))
        logout_button.click()
        login_title = WebDriverWait(driver, MEDIUM_WAIT).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert login_title.is_displayed(), "Заголовок страницы входа не отображается"
        assert 'login' in driver.current_url, f"URL не содержит 'login': {driver.current_url}"