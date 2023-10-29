import allure
from allure_commons.types import AttachmentType
from Login.Locators import *
from time import sleep
from test_utils import wait_until_element_is_enabled


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        wait_until_element_is_enabled(self.driver, 'xpath', mainpage_button_xpath, 5)
