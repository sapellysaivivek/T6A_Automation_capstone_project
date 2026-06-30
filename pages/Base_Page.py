from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from ai.locator_healer import heal_locator

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    NoSuchElementException
)

from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    def find_element(self, by_locator):

        by, value = by_locator

        try:
            return self.wait.until(
            EC.visibility_of_element_located(
                by_locator
            )
        )

        except NoSuchElementException:

            failed_locator = {
                "strategy": str(by),
                "value": value
            }

            return heal_locator(
                self.driver,
                failed_locator
            )


    def click(self, by_locator):

        element = self.find_element(by_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        try:
            element.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def send_keys(self, by_locator, text):

        element = self.find_element(by_locator)

        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):

        element = self.find_element(by_locator)

        return element.text

    def is_visible(self, by_locator):

        try:

            element = self.find_element(by_locator)

            return element.is_displayed()

        except TimeoutException:

            return False

    def select_dropdown(self, by_locator, text):

        dropdown = self.find_element(by_locator)

        select = Select(dropdown)

        select.select_by_visible_text(text)

    def select_dropdown_value(self, by_locator, value):

        dropdown = self.find_element(by_locator)

        select = Select(dropdown)

        select.select_by_value(value)

    def check_checkbox(self, by_locator):

        checkbox = self.find_element(by_locator)

        if not checkbox.is_selected():

            self.click(by_locator)

    def uncheck_checkbox(self, by_locator):

        checkbox = self.find_element(by_locator)

        if checkbox.is_selected():

            self.click(by_locator)

    def get_title(self):

        return self.driver.title

    def get_current_url(self):

        return self.driver.current_url

    def wait_for_url_contains(self, text):

        self.wait.until(
            EC.url_contains(text)
        )


    def wait_for_title_contains(self, text):

        self.wait.until(
            EC.title_contains(text)
        )

  
    def take_screenshot(self, file_name):

        self.driver.save_screenshot(file_name)


 
    def wait_for_element(self, by_locator):

        return self.wait.until(
            EC.visibility_of_element_located(by_locator)
        )

    # CLEAR TEXT FIELD
    def clear_field(self, by_locator):

        element = self.find_element(by_locator)

        element.clear()