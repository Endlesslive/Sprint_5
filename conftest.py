import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'])
def driver(request):
    """
    Фикстура для инициализации WebDriver.
    Параметризована для запуска тестов в разных браузерах.
    """
    browser = request.param
    
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
    
    driver.maximize_window()
    # Убрали implicitly_wait, используем только явные ожидания
    
    yield driver
    
    driver.quit()


@pytest.fixture
def base_url():
    """URL тестируемого приложения"""
    return "https://stellarburgers.education-services.ru/"
