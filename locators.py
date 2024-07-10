from selenium.webdriver.common.by import By


class Locators:
    ENTER_ACCOUNT_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"  #Главная, кнопка "Войти в аккаунт"
    REGISTRATION_BUTTON = By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"  # Личный Кабинет, кнопка
    # "Зарегистрироваться"
    NAME_INPUT = By.XPATH, "//fieldset[1]//div[1]//div[1]//input[1]"  #Поле для ввода имени
    EMAIL_INPUT = By.XPATH, "//fieldset[2]//div[1]//div[1]//input[1]"  #Поле для ввода почты
    PASSWORD_INPUT = By.XPATH, "//fieldset[3]//div[1]//div[1]//input[1]"  #Поле для ввода пароля
    CONFIRM_REGISTRATION_BUTTON = By.XPATH, "//button[contains(text(),'Зарегистрироваться')]"  # Страница
    # регистрации, кнопка "Зарегистрироваться"
    SUCCESSFUL_REGISTRATION = By.XPATH, "//h2[contains(text(),'Вход')]"  # Заголовок "Вход" как маркер успешной
    # регистрации
    INCORRECT_PASSWORD_ERROR = By.XPATH, "//p[@class='input__error text_type_main-default']"  # Текст ошибки о
    # некорректном пароле
    EMAIL_LOGIN_INPUT = By.XPATH, "//input[@name='name']"  #Личный Кабинет, поле для ввода почты(логина)
    PASSWORD_LOGIN_INPUT = By.XPATH, "//input[@name='Пароль']"  #Личный Кабинет, поле для ввода пароля
    ENTER_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"  #Личный Кабинет, кнопка "Войти"
    ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]"  # Главная после авторизации, кнопка
    # "Оформить заказ"
    ACCOUNT_MANAGER = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"  #Главная, кнопка "Личный Кабинет"
    REGISTRATION_FORM_ENTER_BUTTON = By.XPATH, "//a[contains(text(),'Войти')]"  #Форма регистрации, кнопка "Войти"
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"  # Личный кабинет, кнопка
    # "Восстановить пароль"
    BURGER_LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"  # Логотип Stellar
    # Burgers
    BUILDER_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]"  #Кнопка "Конструктор"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(),'Выход')]"  #Личный кабинет, кнопка "Выход"
    BUNS_TAB = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]"  #Вкладка "Булки"
    BUNS_HEADER = By.XPATH, "//h2[contains(text(),'Булки')]"  #Заголовок "Булки"
    SAUSE_TAB = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[2]"  #Вкладка "Соусы"
    SAUSE_HEADER = By.XPATH, "//h2[contains(text(),'Соусы')]"  #Заголовок "Соусы"
    FILLER_TAB = By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/div[1]/div[3]"  #Вкладка "Начинки"
    FILLER_HEADER = By.XPATH, "//h2[contains(text(),'Начинки')]"  #Заголовок "Начинки"
