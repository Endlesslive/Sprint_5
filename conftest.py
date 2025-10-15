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
    SLEEP_AFTER_REGISTRATION,
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
def base_url():
    """URL тестируемого приложения"""
    return BASE_URL

@pytest.fixture
def setup_and_login(driver, base_url):
    """
    Фикстура для создания и входа пользователя перед тестом.
    Используется в тестах, которым требуется авторизованный пользователь.
    """
    # Генерация тестовых данных
    test_email = generate_email()
    test_password = generate_password(8)
    test_name = generate_name()
    
    # Регистрация пользователя
    driver.get(f"{base_url}register")
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
    name_input.send_keys(test_name)
    email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    email_input.send_keys(test_email)
    password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
    password_input.send_keys(test_password)
    register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()
    
    # Ожидание появления формы входа после регистрации
    email_input = WebDriverWait(driver, MEDIUM_WAIT).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(test_email)
    password_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT))
    password_input.clear()
    password_input.send_keys(test_password)
    login_submit_button = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON))
    login_submit_button.click()
    # Проверка успешного входа
    try:
        WebDriverWait(driver, MEDIUM_WAIT).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
    except TimeoutException:
        # Альтернативная проверка - наличие кнопки личного кабинета
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
    # Сохраняем данные пользователя для использования в тестах
    driver.test_email = test_email
    driver.test_password = test_password
    driver.test_name = test_name
    yield driver