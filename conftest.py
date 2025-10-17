import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from constants import (
    BASE_URL,
    DEFAULT_BROWSER,
    SUPPORTED_BROWSERS,
    IMPLICIT_WAIT,
    PAGE_LOAD_TIMEOUT,
    DEFAULT_TIMEOUT,
    MEDIUM_WAIT
)
from helpers.generators import generate_email, generate_password, generate_name
from locators.page_locators import (
    RegistrationPageLocators,
    LoginPageLocators,
    MainPageLocators
    )

@pytest.fixture(params=[DEFAULT_BROWSER])
def driver(request):
    """
    Фикстура для инициализации WebDriver.
    Параметризована для запуска тестов в разных браузерах.
    """
    browser = request.param
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Браузер {browser} не поддерживается")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    yield driver
    driver.quit()

@pytest.fixture
def test_credentials():
    """
    Фикстура для генерации тестовых учетных данных.
    Используется для создания уникального пользователя в каждом тесте.
    """
    return {
        'email': generate_email(),
        'password': generate_password(8),
        'name': generate_name()
    }

@pytest.fixture
def register_user(driver, test_credentials):
    """
    Фикстура для регистрации нового пользователя.
    Выполняет регистрацию и возвращает учетные данные.
    """
    driver.get(f"{BASE_URL}register")
    
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
    name_input.send_keys(test_credentials['name'])
    email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys(test_credentials['email'])
    password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys(test_credentials['password'])
    register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()
    WebDriverWait(driver, MEDIUM_WAIT).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
    return test_credentials


@pytest.fixture
def login_user(driver):
    """
    Фикстура для входа пользователя с заданными учетными данными.
    Возвращает функцию для входа с произвольными учетными данными.
    """
    def _login(email, password):
        driver.get(f"{BASE_URL}login")
        email_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        password_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        login_submit_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON))
        login_submit_button.click()
        WebDriverWait(driver, MEDIUM_WAIT).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
    return _login

@pytest.fixture
def authorized_user(driver):
    """Creates, registers, and logs in a user in the browser"""
    from constants import SLEEP_AFTER_REGISTRATION
    import time
    
    # Generate credentials
    user_data = {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_name()
    }
    
    # Step 1: Register the user
    driver.get(f"{BASE_URL}register")
    
    # Fill registration form
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
    name_input.send_keys(user_data['name'])
    
    email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys(user_data['email'])
    
    password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys(user_data['password'])
    
    register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()
    
    # Признак окончания регистрации: появилась форма логина
    WebDriverWait(driver, MEDIUM_WAIT).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
    
    # Пауза для обработки регистрации на сервере
    time.sleep(SLEEP_AFTER_REGISTRATION)
    
    # Step 2: Login with the registered user
    email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
    email_input.clear()
    email_input.send_keys(user_data['email'])
    
    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    password_input.clear()
    password_input.send_keys(user_data['password'])
    
    login_submit_button = driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON)
    login_submit_button.click()
    
    # Признак успешного входа: кнопка личного кабинета стала кликабельной
    WebDriverWait(driver, MEDIUM_WAIT).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
    
    yield user_data

