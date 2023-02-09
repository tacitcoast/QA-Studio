"""
Common
"""
import time
from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class CommonHelper():
    """
    Common helper class
    """
    def __init__(self, driver):
        self.driver = driver

    def enter_input(self, input_id, data):
        """
        Method for input
        """
        input_field = self.driver.find_element(By.ID, value=input_id)
        input_field.click()
        input_field.send_keys(data)
        time.sleep(1)
        return input_field
        