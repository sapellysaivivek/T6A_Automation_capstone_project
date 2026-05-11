import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from config.config import ECXE, BROWSER, BASE_URL


def get_driver():

    if ECXE == "remote":

        if BROWSER == "chrome":

            options = webdriver.ChromeOptions()

            # REQUIRED FOR DOCKER / GRID
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options
            )

    else:

        if BROWSER == "chrome":

            options = webdriver.ChromeOptions()

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

    driver.get(BASE_URL)

    driver.maximize_window()

    return driver