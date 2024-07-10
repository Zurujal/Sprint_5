
import pytest
from faker import Faker
from random import randint
from selenium import webdriver
from locators import Locators


@pytest.fixture
def name():
    fake = Faker()
    return fake.name()


@pytest.fixture
def email():
    return f'kuznetsovsergei11{randint(000, 999)}@ya.ru'


@pytest.fixture
def password():
    return "".join(chr(randint(33, 125)) for _ in range(12))


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = '/Users/zurujal/Downloads/yandexdriver'
    service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file)
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def auth(driver):
    email = "Ktulhu@ya.ru"
    password = "Ktulhu123"
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(password)
    driver.find_element(*Locators.ENTER_BUTTON).click()
    return auth
