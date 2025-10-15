import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.page_locators import MainPageLocators
from constants import DEFAULT_TIMEOUT


class TestConstructor:
    """Тесты функциональности конструктора"""
    
    def test_navigate_to_buns_section(self, driver, base_url):
        """Тест перехода к разделу 'Булки'"""
        driver.get(base_url)
        # Ожидание загрузки страницы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        # Клик по другому разделу (например, "Соусы")
        sauces_section = driver.find_element(*MainPageLocators.SAUCES_SECTION)
        sauces_section.click()
        # Клик по разделу "Булки"
        buns_section = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION))
        buns_section.click()
        # Проверка активности раздела "Булки"
        active_tab = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text
    
    def test_navigate_to_sauces_section(self, driver, base_url):
        """Тест перехода к разделу 'Соусы'"""
        driver.get(base_url)
        # Ожидание загрузки страницы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        # Клик по разделу "Соусы"
        sauces_section = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION))
        sauces_section.click()
        # Проверка активности раздела "Соусы"
        active_tab = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text
    
    def test_navigate_to_fillings_section(self, driver, base_url):
        """Тест перехода к разделу 'Начинки'"""
        driver.get(base_url)
        # Ожидание загрузки страницы
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        # Клик по разделу "Начинки"
        fillings_section = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION))
        fillings_section.click()
        # Проверка активности раздела "Начинки"
        active_tab = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text
