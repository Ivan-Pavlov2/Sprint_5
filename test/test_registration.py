from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import helper
import data

class TestRegistration:

    def test_registration_with_correct_data_successful(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.NAME).send_keys(data.name)
        helper.insert_reg(browser)
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.url_contains("/login"))
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_without_name_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        helper.insert_reg(browser)
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/register"
        assert browser.find_element(*TestLocators.NAME).get_attribute("value") == ""

    def test_registration_with_short_password_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.NAME).send_keys("Женя")
        browser.find_element(*TestLocators.EMAIL).send_keys(helper.generate_login() + '@yandex.ru')
        password = helper.generate_password()[:-3]
        browser.find_element(*TestLocators.PASSWORD).send_keys(password)
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_ERROR))
        assert browser.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'

    def test_registration_with_bad_email_failed(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        browser.find_element(*TestLocators.NAME).send_keys("Женя")
        browser.find_element(*TestLocators.EMAIL).send_keys(helper.generate_login())
        browser.find_element(*TestLocators.PASSWORD).send_keys(helper.generate_password())
        browser.find_element(*TestLocators.REGISTR_BUTTON).click()
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_ERROR))
        assert browser.find_element(*TestLocators.EMAIL_ERROR).text == 'Такой пользователь уже существует'
