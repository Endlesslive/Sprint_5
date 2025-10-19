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
from constants import BASE_URL

class TestPersonalAccount:
    """Тесты функциональности личного кабинета"""     
    def test_navigate_to_personal_account(self, driver, authorized_user):
        """Тест перехода в личный кабинет"""
        # Клик по кнопке "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        # Проверка перехода в личный кабинет
        profile_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE))
        assert profile_title.is_displayed()
    
    def test_navigate_from_account_to_constructor_via_button(self, driver, authorized_user):
        """Тест перехода из личного кабинета в конструктор по кнопке"""
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE))
        # Клик по кнопке "Конструктор"
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()
        # Проверка перехода в конструктор
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert constructor_title.is_displayed()
    
    def test_navigate_from_account_to_constructor_via_logo(self, driver, authorized_user):
        """Тест перехода из личного кабинета в конструктор по логотипу"""
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(PersonalAccountPageLocators.PROFILE_TITLE))
        # Клик по логотипу Stellar Burgers
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO))
        logo.click()
        # Проверка перехода в конструктор
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert constructor_title.is_displayed()