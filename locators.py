from selenium.webdriver.common.by import By


class TestLocators:

    REGISTRATION = By.LINK_TEXT, "Зарегистрироваться"  # Ссылка на форму регистации
    NAME = By.XPATH, "//*[text()='Имя']/following-sibling::input"  # Поле ввода имени
    EMAIL = By.XPATH, "//*[text()='Email']/following-sibling::input"  # Поле ввода почты
    PASSWORD = By.NAME, "Пароль"  # Поле ввода пароля
    REGISTR_BUTTON = By.XPATH, './/*[contains(@class, "button_button_type_primary")]'  # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = By.XPATH, ".//*[contains(text(),'Некорректный пароль')]"  # ошибка пароля
    EMAIL_ERROR = By.XPATH, ".//*[contains(text(),'Такой пользователь уже существует')]" # неверный email
    PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, "Личный Кабинет"  # Кнопка 'Личный Кабинет'
    ENTER_LINK_BUTTON = By.LINK_TEXT, "Войти"  # Кнопка войти с формы регистрации и восстановления пароля
    ENTER_IN_ACCOUNT_BUTTON = By.XPATH, '//*[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    ENTER_BUTTON = By.XPATH, './/*[contains(@class, "button_button_type_primary") and contains(text(), "Войти")]'  # Кнопка 'Войти'
    FORGOT_PASSWORD = By.LINK_TEXT, "Восстановить пароль"  # Ссылка на форму восстановления
    ORDER_BUTTON = By.XPATH, '//*[contains(text(), "Оформить заказ")]'
    LOGIN_FIELD = By.XPATH, ".//*[text()='Логин']/following-sibling::input"
    ACCOUNT_LIST = By.XPATH, '//*[contains(@class, "Account_list_")]'  # пункты личного кабинета
    CONSTRUCTOR_COLUMN = By.XPATH, '//*[contains(@class, "AppHeader_header") and contains(text(), "Конструктор")]'  # Страница 'Конструктор'
    CHOOSE_BREAD = By.XPATH, ".//*[contains(text(), 'Перетяните булочку сюда (верх)')]"   # Перетяните булочку
    LOGO = By.XPATH, '//*[contains(@class, "AppHeader_header__logo")]'  # Логотип
    LOGOUT_BUTTON = By.XPATH, '//*[text()="Выход"]'  # Кнопка 'Выход'
    BREAD_BUTTON = By.XPATH, "//span[text()='Булки']/parent::*"  # Кнопка булок
    SAUCES_BUTTON = By.XPATH, "//span[text()='Соусы']/parent::*"  # Кнопка соусов
    FILLINGS_BUTTON = By.XPATH, "//span[text()='Начинки']/parent::*"  # Кнопка начинок
