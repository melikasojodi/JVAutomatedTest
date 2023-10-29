import allure
from allure_commons.types import AttachmentType
from Login.Locators import *
from time import sleep

from test_utils import wait_until_element_is_enabled


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        wait_until_element_is_enabled(self.driver, 'id', username_textbox_id, 5)
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        wait_until_element_is_enabled(self.driver, 'id', password_textbox_id, 5)
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_login_button(self):
        wait_until_element_is_enabled(self.driver, 'class name', login_button_classname, 5)

    def massage_eror_invalid_login(self):
        wait_until_element_is_enabled(self.driver, 'xpath', invalid_login_xpath, 5)

    def massage_eror_blank_usernamepassword(self):
        wait_until_element_is_enabled(self.driver, 'xpath', blank_username_password, 5)
