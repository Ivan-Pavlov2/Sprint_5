from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
import data

class TestOpenAccountPage:

    def test_go_to_account_unregistered(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_go_to_account_registered(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/account/profile"))
        browser.find_element(*TestLocators.ACCOUNT_LIST)
        assert browser.find_element(*TestLocators.LOGIN_FIELD).get_attribute("value") == data.email
