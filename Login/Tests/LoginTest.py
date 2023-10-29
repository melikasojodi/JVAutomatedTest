from Login.Pages.Login import Login
from selenium import webdriver
from time import sleep
from Login.Pages.MainPage import MainPage
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from pathlib import Path
import os


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.options = Options()
        cls.options.add_argument("--window-size=1366,768")
        cls.options.add_argument("--headless")
        cls.options.add_argument("--no-sandbox")
        cls.service = Service(
            executable_path='/var/lib/jenkins/.wdm/drivers/chromedriver/linux64/112.0.5615/chromedriver')
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        root_path = Path(__file__).parent.parent.parent
        config_file_path = os.path.join(root_path, 'Config.json')
        with open(config_file_path, 'r') as config_file:
            cls.config = json.load(config_file)

    def test_valid_login(self):
        self.driver.get(self.config["Links"]["base_url"])
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.login_button()
        login.enter_username(self.config["User"]["username"])
        login.next_step()
        login.enter_password(self.config["User"]["password"])
        login.submit()
        sleep(3)
        main_page.check_main_page()

        sleep(3)

    def test_invalid_username(self):
        self.driver.get(self.config["Links"]["base_url"])
        login = Login(driver=self.driver)
        login.login_button()
        login.enter_username("0000")
        login.next_step()
        login.error_massage_invalid_username()

    def test_invalid_password(self):
        self.driver.get(self.config["Links"]["base_url"])
        login = Login(driver=self.driver)
        login.login_button()
        login.enter_username(self.config["User"]["username"])
        login.next_step()
        login.enter_password("0000")
        login.submit()
        login.error_massage_invalid_password()

        # sleep(3)

    def test_login_blank_username(self):
        self.driver.get(self.config["Links"]["base_url"])
        login = Login(driver=self.driver)
        login.login_button()
        login.next_step()
        login.error_massage_blank_username()

        # sleep(3)

    def test_login_blank_password(self):
        self.driver.get(self.config["Links"]["base_url"])
        login = Login(driver=self.driver)
        login.login_button()
        login.enter_username(self.config["User"]["username"])
        login.next_step()
        login.submit()
        login.error_massage_invalid_password()

        # sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
