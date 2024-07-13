
import data
import helpers
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_valid_password(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(helpers.generate_name())
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(helpers.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(helpers.generate_password())
        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SUCCESSFUL_REGISTRATION))
        assert driver.find_element(*Locators.SUCCESSFUL_REGISTRATION).text == "Вход"

    def test_registration_wrong_password(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(helpers.generate_name())
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(helpers.generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(data.WRONG_PASSWORD)
        driver.find_element(*Locators.CONFIRM_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INCORRECT_PASSWORD_ERROR))
        assert driver.find_element(*Locators.INCORRECT_PASSWORD_ERROR).text == "Некорректный пароль"
