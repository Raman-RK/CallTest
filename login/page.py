from helpers.base_page import *
import login.locators as loc
from utilities.customer_logger import *


class Login(CommonClass):
    bp = Base()

    def add_username(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.email, text)

    def add_password(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.password, text)

    def click_signin(self):
        self.click_element('CSS_SELECTOR', loc.sign_in_button)

    def wait_to_verify_user_is_on_dashboard(self):
        self.wait_for_visibility('CSS_SELECTOR', loc.dashboard)

    def get_icon(self, row="last()", col="last()", btn="last()"):
        """
        Get a specific icon in a table based on row, column, and button index.

        :param row: Row number or 'last()'
        :param col: Column number or 'last()'
        :param btn: Button index inside the column or 'last()'
        :return: WebElement (icon)
        """
        css = f"table > tbody > tr:nth-child({row}) > td:nth-child({col}) > div > div > button:nth-child({btn}) > div > svg"
        self.logger.info(f"Locating icon at row={row}, col={col}, button={btn}")
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
