from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    # Заголовок "Соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    # Раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    
    # Раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    
    # Раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    
    # Активный таб (для проверки текущего раздела)
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    # Заголовок "Вход"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Кнопка "Войти"
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    
    # Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Заголовок "Регистрация"
    REGISTRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    
    # Поле "Имя"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    
    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Сообщение об ошибке "Некорректный пароль"
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class PasswordRecoveryPageLocators:
    """Локаторы страницы восстановления пароля"""
    
    # Заголовок "Восстановление пароля"
    RECOVERY_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class PersonalAccountPageLocators:
    """Локаторы страницы личного кабинета"""
    
    # Заголовок профиля
    PROFILE_TITLE = (By.XPATH, "//a[text()='Профиль']")
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Ссылка "История заказов"
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
