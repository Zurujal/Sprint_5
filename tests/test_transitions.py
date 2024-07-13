
import data
from locators import Locators



class TestTransitions:

    def test_builder_account_transition(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        assert driver.find_element(*Locators.REGISTRATION_BUTTON).text == "Зарегистрироваться"

    def test_account_burger_logo_transition(self, driver):
        driver.get(data.LOGIN_PAGE_URL)
        driver.find_element(*Locators.BURGER_LOGO).click()
        assert driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).text == "Войти в аккаунт"

    def test_account_builder_transition(self, driver):
        driver.get(data.LOGIN_PAGE_URL)
        driver.find_element(*Locators.BUILDER_BUTTON).click()
        assert driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).text == "Войти в аккаунт"
