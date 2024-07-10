from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

email = "Ktulhu@ya.ru"
password = "Ktulhu123"


class TestLogin:

    def test_login_account_button(self, driver, auth):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_account_manager(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.ACCOUNT_MANAGER).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_registration_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_FORM_ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"

    def test_login_recover_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_FORM_ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).text == "Оформить заказ"
