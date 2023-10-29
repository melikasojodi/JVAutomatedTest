import allure
from allure_commons.types import AttachmentType
from Login.Locators import *
from time import sleep

from test_utils import wait_until_element_is_enabled


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login_button(self):
        wait_until_element_is_enabled(self.driver, 'xpath', login_button, 5)

    def enter_username(self, username):
        wait_until_element_is_enabled(self.driver, 'name', username_textbox, 5)
        self.driver.find_element('name', username_textbox).send_keys(username)

    def next_step(self):
        wait_until_element_is_enabled(self.driver, 'xpath', next_step, 5)

    def enter_password(self, password):
        wait_until_element_is_enabled(self.driver, 'name', password_textbox, 5)
        self.driver.find_element('name', password_textbox).send_keys(password)

    def submit(self):
        wait_until_element_is_enabled(self.driver, 'xpath', submit, 5)

    def error_massage_invalid_username(self):
        wait_until_element_is_enabled(self.driver, 'xpath', invalid_username, 5)

    def error_massage_invalid_password(self):
        wait_until_element_is_enabled(self.driver, 'xpath', invalid_password, 5)

    def error_massage_blank_username(self):
        wait_until_element_is_enabled(self.driver, 'xpath', blank_username, 5)

    def error_massage_blank_password(self):
        wait_until_element_is_enabled(self.driver, 'xpath', blank_password, 5)
