from locators import TestLocators

class TestConstructor:

    def test_constructor_select_sause(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.SAUCES_BUTTON).click()
        is_active = browser.find_element(*TestLocators.SAUCES_BUTTON).get_attribute('class')
        assert 'current' in is_active

    def test_constructor_select_bread(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.SAUCES_BUTTON).click()
        browser.find_element(*TestLocators.BREAD_BUTTON).click()
        is_active = browser.find_element(*TestLocators.BREAD_BUTTON).get_attribute('class')
        assert 'current' in is_active

    def test_constructor_select_fillings(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.FILLINGS_BUTTON).click()
        is_active = browser.find_element(*TestLocators.FILLINGS_BUTTON).get_attribute('class')
        assert 'current' in is_active
        