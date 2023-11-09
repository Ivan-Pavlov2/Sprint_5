import random
import string
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import data

def generate_login():
    characters = string.ascii_lowercase
    login = ''.join(random.choice(characters) for _ in range(8))
    return login

def generate_password():
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

def insert_login(browser):
    browser.find_element(*TestLocators.EMAIL).send_keys(data.email)
    browser.find_element(*TestLocators.PASSWORD).send_keys(data.password)
    browser.find_element(*TestLocators.ENTER_BUTTON).click()
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    browser.find_element(*TestLocators.ORDER_BUTTON)
    return (browser)

def insert_reg(browser):
    browser.find_element(*TestLocators.EMAIL).send_keys(generate_login() + '@yandex.ru')
    browser.find_element(*TestLocators.PASSWORD).send_keys(generate_password())
    return (browser)