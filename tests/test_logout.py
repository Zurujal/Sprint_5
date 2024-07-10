
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:

    def test_logout_account_button(self, driver, auth):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_MANAGER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert driver.find_element(*Locators.REGISTRATION_BUTTON).text == "Зарегистрироваться"
