from time import sleep
import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException


def wait_until_element_is_enabled(driver, selector, locator, timeout):
    for i in range(timeout * 3):
        try:
            sleep(0.5)
            element = driver.find_element(selector, locator)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("window.scrollBy(0,-200);")
            element.click()
            return
        except:
            sleep(0.5)
            if i == 14:
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
                raise TimeoutException(f"Timed out waiting for element {selector}='{locator}' to be clickable")
