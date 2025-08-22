import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import *


class Base:
    def __init__(self, domain="@gmail.com"):
        self.domain = domain

    @staticmethod
    def pick_random_number():
        number_list = ("+918699916843", "+918894988689")
        random_number = random.choice(number_list)
        return random_number

class CommonClass:
    config = ConfigManager()
    baseURL = config.get_url('WEBSITE')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator_strategy, locator_value, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator_value))
        )

    def click_element(self, locator_strategy, locator_value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((getattr(By, locator_strategy), locator_value))
        )
        element.click()

    def send_keys_to_element(self, locator_strategy, locator_value,input_text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator_value))
        )
        element.clear()
        element.send_keys(input_text)

    def get_text_from_element(self, locator_strategy, locator_value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator_value))
        )
        element_text = element.text
        return element_text

