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
logger = get_logger(__name__)
allure.feature("Home Page Tests")

#TC-06 note-01 - Verify that a user can create a new note with valid inputs.
@pytest.mark.ui
def test_add_note( driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","This is a test note.",True)
    bp = BasePage(driver)

    assert bp.is_visible((By.XPATH, "//div[@data-testid='note-card-title' and text()='Test_Note']"))
    home_page_obj.delete_note("Test_Note")
#TC-07 note-02 - Verify that a user cannot create a note with empty title .
@pytest.mark.ui
def test_add_note_empty_title(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","","This is a test note.",True)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[contains(text(),'Title is required')]"))
 
#TC-08 note-03 - Verify that a user cannot create a note with empty description.
@pytest.mark.ui
def test_add_note_empty_description(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","",True)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[contains(text(),'Description is required')]"))
    
# note-04 - Verify that a user can cancel the note creation process.
@pytest.mark.ui
def test_cancel_note_creation( driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.click_add_notes()
    home_page_obj.click_cancel()
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//button[text()='+ Add Note']"))
    
# note-05 - Verify that a user can create a note without marking it as completed.
@pytest.mark.ui

def test_add_note_without_completed(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","This is a test note.",False)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[@data-testid='note-card-title' and text()='Test_Note']"))
    home_page_obj.delete_note("Test_Note")
#TC-09 notes-06 - Verify that a user can log in and access his notes.
@pytest.mark.api
def test_get_notes(token):
    response = get("https://practice.expandtesting.com/notes/api/notes/", token)
    assert response.status_code == 200
    assert "data" in response.json()
#TC-10 notes-07 - Verify new user has no notes.
@pytest.mark.api
def test_new_user_no_notes():

    register_response = post(
        "https://practice.expandtesting.com/notes/api/users/register",
        {
            "name": "Sapelyy Sai Vivek",
            "email": "saiviveksapelly1222@gmail.com",
            "password": "789456123"
        }
    )

    print(register_response.json())

    login_response = login_api("saiviveksapelly1222@gmail.com", "789456123")

    print(login_response.json())

    token = login_response.json().get("data", {}).get("token")

    response = get(
        "https://practice.expandtesting.com/notes/api/notes/",
        token
    )

    print(response.json())

    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) == 0

#TC-11 notes-08 - Verify that ui created note appears in the notes list retrieved via API.
@pytest.mark.ui
@pytest.mark.api
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


#TC-12 & TC-13 notes-09 - Verify that user delete with id is deleted successfully via API.
@pytest.mark.api
def test_delete_note_api(token):
    create_response = create_note_api(token, "Test_Note", "This is a test note.", "Work", False)

    assert create_response.status_code == 200
    note_id = create_response.json().get("data", {}).get("id")

    delete_response = delete_note_api(token, note_id)

    assert delete_response.status_code == 200

    get_response = get(
        f"https://practice.expandtesting.com/notes/api/notes/{note_id}",
        token
    )

    assert get_response.status_code == 404
#TC-14 Deleted note via API should not be visible in UI.
@pytest.mark.ui
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
#TC-15 response times for /api/notes/ endpoint should be within 2s.
@pytest.mark.api
def test_notes_api_response_time(token):
    start_time = time.time()
    response = get("https://practice.expandtesting.com/notes/api/notes/", token)
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 2, f"API response time was {(end_time - start_time)} seconds, which is longer than the expected 2 seconds."
#TC-16 Verify that post /notes/ endpoint creates note successfully and returns correct data within 2s.
@pytest.mark.api
def test_create_note_api_response_time(token):
    start_time = time.time()
    response = create_note_api(token, "Test_Note", "This is a test note.", "Work", False)
    end_time = time.time()
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["title"] == "Test_Note"
    assert (end_time - start_time) < 2, f"API response time was {(end_time - start_time)} seconds, which is longer than the expected 2 seconds."
#TC-17 Verify that delete /notes/{id} endpoint deletes note successfully and returns correct status code within 2s.
@pytest.mark.api
def test_delete_note_api_response_time(token):
    create_response = create_note_api(token, "Test_Note", "This is a test note.", "Work", False)
    assert create_response.status_code == 200
    note_id = create_response.json().get("data", {}).get("id")
    start_time = time.time()
    delete_response = delete_note_api(token, note_id)
    end_time = time.time()
    assert delete_response.status_code == 200
    assert (end_time - start_time) < 2, f"API response time was {(end_time - start_time)} seconds, which is longer than the expected 2 seconds."
#TC-18 Verify that get /notes/ endpoint returns status code 404 on unauthorized access 
@pytest.mark.api
def test_get_notes_unauthorized():
    response = get("https://practice.expandtesting.com/notes/api/notes/", token=None)
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, but got {response.status_code}."
#TC-20 create note with whitespace title 
@pytest.mark.ui
def test_create_note_whitespace_title(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","           ","This is a test note with whitespace title.",True)
    bp = BasePage(driver)
    if bp.is_visible((By.XPATH, "//div[contains(text(),'Title must be between 4 and 100 characters')]")) or bp.is_visible((By.XPATH, "//div[contains(text(),'Title should be between 4 and 100 characters')]")):
        logger.info("Proper validation message is displayed for whitespace title.")
        assert True

#TC-21 get note with invalid token
@pytest.mark.api
def test_get_notes_invalid_token():
    invalid_token = "invalid_token_example"
    response = get("https://practice.expandtesting.com/notes/api/notes/", token=
invalid_token)
    assert response.status_code == 401, f"Expected status code 401 for invalid token, but got {response.status_code}."
#TC-22 deleting note with invalid token 
@pytest.mark.api
def test_delete_note_invalid_token():
    invalid_token = "invalid_token_example"
    create_response = create_note_api(invalid_token, "Test_Note", "This is a test note.", "Work", False)
    assert create_response.status_code == 401, f"Expected status code 401 for invalid token during note creation, but got {create_response.status_code}."
#TC-23 create note with special characters in title
@pytest.mark.ui
def test_create_note_special_characters_title(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com", "142536475869")
    home_page_obj = home_page.HomePage(driver)
    special_title = "!@#$%^&*()_+{}|:\"<>?`~"
    home_page_obj.create_note("Work", special_title, "This is a test note with special characters in the title.", True)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, f"//div[@data-testid='note-card-title' and text()='{special_title}']"))
#TC-24 create note with very long title
@pytest.mark.uii
def test_create_note_long_title(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com", "142536475869")
    home_page_obj = home_page.HomePage(driver)
    long_title = "A" * 101  # 101 characters long
    home_page_obj.create_note("Work", long_title, "This is a test note with a very long title.", True)
    bp = BasePage(driver)
    if bp.is_visible((By.XPATH, "//div[contains(text(),'Title must be between 4 and 100 characters')]")) or bp.is_visible((By.XPATH, "//div[contains(text(),'Title should be between 4 and 100 characters')]")):
        logger.info("Proper validation message is displayed for long title.")
        assert True
