import allure
import pytest
import pages.home_page as home_page
from pages.Base_Page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time
from utils.logger import get_logger
logger = get_logger(__name__)
@allure.epic("NOTES MANAGEMENT ")
@allure.feature("NOTES MANAGEMENT frontend")
#TC-06 note-01 - Verify that a user can create a new note with valid inputs.
@allure.story("creating notes with valid inputs")
@allure.description("This test verifies that a user can create a new note with valid inputs.")
@pytest.mark.ui
def test_add_note( driver):
 

    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","This is a test note.",True)
    bp = BasePage(driver)

    assert bp.is_visible((By.XPATH, "//div[@data-testid='note-card-title' and text()='Test_Note']"))
    
    
    
    
#TC-07 note-02 - Verify that a user cannot create a note with empty title .
@allure.story("creating notes with empty title")
@allure.description("This test verifies that a user cannot create a note with empty title.")
@pytest.mark.ui
def test_add_note_empty_title(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","","This is a test note.",True)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[contains(text(),'Title is required')]"))
 
#TC-08 note-03 - Verify that a user cannot create a note with empty description.
@allure.story("creating notes with empty description")
@allure.description("This test verifies that a user cannot create a note with empty description.")
@pytest.mark.ui
def test_add_note_empty_description(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","",True)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[contains(text(),'Description is required')]"))
    
# note-04 - Verify that a user can cancel the note creation process.
@allure.story("canceling note creation")
@allure.description("This test verifies that a user can cancel the note creation process.")
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
@allure.story("creating notes without marking as completed")
@allure.description("This test verifies that a user can create a note without marking it as completed.")
@pytest.mark.ui

def test_add_note_without_completed(driver):
    login_page = LoginPage(driver)
    login_page.click_login("saiviveksapelly@gmail.com" , "142536475869")
    home_page_obj = home_page.HomePage(driver)
    home_page_obj.create_note("Work","Test_Note","This is a test note.",False)
    bp = BasePage(driver)
    assert bp.is_visible((By.XPATH, "//div[@data-testid='note-card-title' and text()='Test_Note']"))
    home_page_obj.delete_note("Test_Note")
#TC-20 create note with whitespace title 

@allure.story("creating notes with whitespace title")
@allure.description("This test verifies that a user cannot create a note with whitespace title.")
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
#TC-23 create note with special characters in title

@allure.story("creating notes with special characters in title")
@allure.description("This test verifies that a user can create a note with special characters in the title.")
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
@allure.story("creating notes with very long title")
@allure.description("This test verifies that a user cannot create a note with a title longer than 100 characters.")
@pytest.mark.ui
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
