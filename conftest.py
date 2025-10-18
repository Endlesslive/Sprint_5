import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from constants import (
    BASE_URL,
    DEFAULT_BROWSER,
    SUPPORTED_BROWSERS,
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
    browser = request.param
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Браузер {browser} не поддерживается")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    yield driver
    driver.quit()

@pytest.fixture
def test_credentials():
    return {
        'email': generate_email(),
        'password': generate_password(8),
        'name': generate_name()
    }

@pytest.fixture
def register_user(driver, test_credentials):
    driver.get(f"{BASE_URL}register")
    try:
        name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
        name_input.send_keys(test_credentials['name'])
    except TimeoutException:
        raise TimeoutException(f"Name input not found at {BASE_URL}register")
    try:
        email_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT))
        email_input.send_keys(test_credentials['email'])
    except TimeoutException:
        raise TimeoutException(f"Email input not found at {BASE_URL}register")
    try:
        password_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT))
        password_input.send_keys(test_credentials['password'])
    except TimeoutException:
        raise TimeoutException(f"Password input not found at {BASE_URL}register")
    try:
        register_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON))
        register_button.click()
    except TimeoutException:
        raise TimeoutException(f"Register button not found at {BASE_URL}register")
    try:
        WebDriverWait(driver, MEDIUM_WAIT).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
    except TimeoutException:
        raise TimeoutException("Login page not loaded after registration")
    return test_credentials

@pytest.fixture
def login_user(driver):
    def _login(email, password):
        driver.get(f"{BASE_URL}login")
        try:
            email_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
            email_input.clear()
            email_input.send_keys(email)
        except TimeoutException:
            raise TimeoutException(f"Email input not found at {BASE_URL}login")
        try:
            password_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT))
            password_input.clear()
            password_input.send_keys(password)
        except TimeoutException:
            raise TimeoutException(f"Password input not found at {BASE_URL}login")
        try:
            login_submit_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON))
            login_submit_button.click()
        except TimeoutException:
            raise TimeoutException(f"Login button not found at {BASE_URL}login")
        try:
            WebDriverWait(driver, MEDIUM_WAIT).until(
                EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        except TimeoutException:
            raise TimeoutException("Personal account button not found after login")
    return _login

@pytest.fixture
def authorized_user(driver, register_user, login_user):
    login_user(register_user['email'], register_user['password'])
    yield register_user