
import pytest
import data
from selenium import webdriver
from locators import Locators


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = './yandexdriver'
    service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file)
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def auth(driver):
    driver.get(data.HOME_PAGE_URL)
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(data.EMAIL)
    driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(data.PASSWORD)
    driver.find_element(*Locators.ENTER_BUTTON).click()
