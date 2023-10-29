from Login.Pages.Login import Login
from selenium import webdriver
from time import sleep
from Login.Pages.MainPage import MainPage
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
        self.driver.get(self.config["Links"]["base_url"] + "/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        login.enter_username(self.config["SecondTerm"]["username"])
        sleep(3)
        login.enter_password(self.config["SecondTerm"]["password"])
        sleep(3)
        login.click_on_login_button()
        sleep(3)
        main_page.check_main_page()

        sleep(3)

    def test_invalid_login(self):
        self.driver.get(self.config["Links"]["base_url"] + "/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        sleep(5)
        self.driver.refresh()
        sleep(3)
        login.enter_username("0000")
        login.enter_password("0000")
        sleep(3)
        login.click_on_login_button()
        sleep(3)
        login.massage_eror_invalid_login()

        # sleep(3)

    def test_login_blank_username(self):
        self.driver.get(self.config["Links"]["base_url"] + "/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        sleep(3)
        login.enter_password("0020421729")
        sleep(3)
        login.click_on_login_button()
        sleep(3)
        login.massage_eror_blank_usernamepassword()

        # sleep(3)

    def test_login_blank_password(self):
        self.driver.get(self.config["Links"]["base_url"] + "/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        sleep(3)
        login.enter_username("7418700")
        sleep(3)
        login.click_on_login_button()
        login.massage_eror_blank_usernamepassword()

        # sleep(3)

    def test_login_blank_username_password(self):
        self.driver.get(self.config["Links"]["base_url"] + "/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        sleep(3)
        login.click_on_login_button()
        sleep(3)
        login.massage_eror_blank_usernamepassword()

        # sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
