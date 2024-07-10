from locators import Locators


class TestBuilder:

    def test_buns_transitions(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUNS_TAB).click()
        assert driver.find_element(*Locators.BUNS_HEADER).text == "Булки"

    def test_sauses_transitions(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SAUSE_TAB).click()
        assert driver.find_element(*Locators.SAUSE_HEADER).text == "Соусы"

    def test_filler_transitions(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.FILLER_TAB).click()
        assert driver.find_element(*Locators.FILLER_HEADER).text == "Начинки"
