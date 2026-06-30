import pytest
import allure

from config.config import BROWSERS
from fixtures.browser_fixture import get_driver
from fixtures.get_token import get_token
@pytest.fixture(scope="function" , params=BROWSERS)
def driver(request):
    
    driver = get_driver(request.param)
    
    yield driver

    driver.quit()
@pytest.fixture(scope="function")
def token():
    token = get_token("saiviveksapelly@gmail.com", "142536475869")
    yield token
    token = None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Could not capture screenshot: {e}")