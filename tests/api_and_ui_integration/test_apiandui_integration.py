import allure
import pytest
import pages.home_page as home_page
from pages.Base_Page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from fixtures.auth_client import *
from pages.notes_api import *
import time
from utils.logger import get_logger
#TC-14 Deleted note via API should not be visible in UI.
@allure.feature("NOTES MANAGEMENT frontend and API")
@allure.story("deleted note not visible in ui")
@allure.description("This test verifies that a note deleted via the API is not visible in the UI.")
@pytest.mark.uiandapi
def test_deleted_note_not_in_ui(driver, token):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com", "142536475869")
    home_page_obj = home_page.HomePage(driver)
    create_response = create_note_api(token, "Test_Note", "This is a test note.", "Work", False)
    assert create_response.status_code == 200
    note_id = create_response.json().get("data", {}).get("id")
    delete_response = delete_note_api(token, note_id)
    assert delete_response.status_code == 200
    driver.refresh()
    assert not home_page_obj.is_note_visible("Test_Note")
#TC-11 notes-08 - Verify that ui created note appears in the notes list retrieved via API.
@allure.story("ui created note appears in api")
@allure.description("This test verifies that a note created via the UI appears in the notes")
@pytest.mark.uiandapi
def test_ui_created_note_in_api(driver, token):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","This is a test note.",True)
    response = get("https://practice.expandtesting.com/notes/api/notes/", token)    
    assert response.status_code == 200
    assert "data" in response.json()
    assert any(note["title"] == "Test_Note" for note in response.json()["data"])
    home_page_obj.delete_note("Test_Note")
#TC-14 Deleted note via API should not be visible in UI.
@allure.feature("NOTES MANAGEMENT frontend and API")
@allure.story("deleted note not visible in ui")
@allure.description("This test verifies that a note deleted via the API is not visible in the UI.")
@pytest.mark.uiandapi
def test_deleted_note_not_in_ui(driver, token):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com", "142536475869")
    home_page_obj = home_page.HomePage(driver)
    create_response = create_note_api(token, "Test_Note", "This is a test note.", "Work", False)
    assert create_response.status_code == 200
    note_id = create_response.json().get("data", {}).get("id")
    delete_response = delete_note_api(token, note_id)
    assert delete_response.status_code == 200
    driver.refresh()
    assert not home_page_obj.is_note_visible("Test_Note")