import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import (
    MainPageLocators, 
    LoginPageLocators, 
    RegistrationPageLocators,
    PasswordRecoveryPageLocators
)
from helpers.generators import generate_email, generate_password, generate_name


class TestLogin:
    """Тесты входа в систему"""
    
    @pytest.fixture(autouse=True)
    def setup_user(self, driver, base_url):
        """Создание тестового пользователя перед каждым тестом"""
        self.test_email = generate_email()
        self.test_password = generate_password(8)
        self.test_name = generate_name()
        
        # Регистрация пользователя
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
        
        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
    
    def test_login_via_main_page_button(self, driver, base_url):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver.get(base_url)
        
        # Клик по кнопке "Войти в аккаунт"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        # Ввод данных и вход
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(self.test_email)
        
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(self.test_password)
        
        login_submit_button = driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()
        
        # Проверка успешного входа
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed()
    
    def test_login_via_personal_account_button(self, driver, base_url):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get(base_url)
        
        # Клик по кнопке "Личный кабинет"
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        # Ввод данных и вход
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(self.test_email)
        
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(self.test_password)
        
        login_submit_button = driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()
        
        # Проверка успешного входа
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed()
    
    def test_login_via_registration_form(self, driver, base_url):
        """Тест входа через кнопку в форме регистрации"""
        driver.get(f"{base_url}register")
        
        # Клик по ссылке "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Ввод данных и вход
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(self.test_email)
        
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(self.test_password)
        
        login_submit_button = driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()
        
        # Проверка успешного входа
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed()
    
    def test_login_via_password_recovery_form(self, driver, base_url):
        """Тест входа через кнопку в форме восстановления пароля"""
        driver.get(f"{base_url}forgot-password")
        
        # Клик по ссылке "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PasswordRecoveryPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        # Ввод данных и вход
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(self.test_email)
        
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(self.test_password)
        
        login_submit_button = driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()
        
        # Проверка успешного входа
        constructor_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )
        assert constructor_title.is_displayed()
