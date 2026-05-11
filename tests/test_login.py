import pytest
from pages.Base_Page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from fixtures.auth_client import *
from utils.logger import get_logger

logger = get_logger(__name__)
#TC-01 Login-01 - Verify that a user can log in with valid credentials.
@pytest.mark.ui
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    Bp = BasePage(driver)
    assert Bp.is_visible((By.XPATH, "//button[text()='Logout']"))
#TC-02 Login-02 - Verify that the session persists.
@pytest.mark.ui
def test_session_maintenance(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    Bp = BasePage(driver)
    driver.refresh()
    assert Bp.is_visible((By.XPATH, "//button[text()='Logout']"))
#TC-03 Login-03 - Verify that a user cannot log in with invalid credentials.
@pytest.mark.ui
def test_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.click_login("invalid_email" , "142536475869")
    Bp = BasePage(driver)
    assert Bp.is_visible((By.XPATH, "//div[contains(text(),'Email address is invalid')]"))
#TC-04 Login-04 - Verify that a user cannot log in with invalid password.
@pytest.mark.ui
def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "invalid_password")
    Bp = BasePage(driver)
    assert Bp.is_visible((By.XPATH, "//div[contains(text(),'Incorrect email address or password')]"))
#TC-05 Login-05 - Verify that a user cannot log in with empty email and password fields.
@pytest.mark.ui
def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.click_login("" , "")
    Bp = BasePage(driver)
    assert Bp.is_visible((By.XPATH, "//div[contains(text(),'Email address is required')]"))
    assert Bp.is_visible((By.XPATH, "//div[contains(text(),'Password is required')]"))
# Login-06 - Verify that a user can log out successfully after logging in.
@pytest.mark.ui
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    Bp = BasePage(driver)
    Bp.click((By.XPATH, "//button[text()='Logout']"))
    assert Bp.is_visible((By.XPATH, "//a[@href='/notes/app/login']"))
@pytest.mark.api
def test_login_api():
    response = post("https://practice.expandtesting.com/notes/api/users/login", {"email": "saiviveksapelly@gmail.com", "password": "142536475869"})
    assert response.status_code == 200
    assert "data" in response.json()
    assert "token" in response.json()["data"]

