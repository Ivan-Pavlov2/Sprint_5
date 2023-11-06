from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import data

class TestLoginPage:

    def test_login_through_personal_account_button(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_by_button_through_enter_account_button(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_through_registration_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.ENTER_LINK_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_through_password_recovery_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.FORGOT_PASSWORD).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/forgot-password"))
        browser.find_element(*TestLocators.ENTER_LINK_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
        browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
        browser.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/"
