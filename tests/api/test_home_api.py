import pytest
import allure
from fixtures.auth_client import *
from pages.notes_api import *
from utils.logger import get_logger
import time
@allure.feature("NOTES MANAGEMENT API")
#TC-09 notes-06 - Verify that a user can log in and access his notes.

@allure.story("accessing notes after login")
@allure.description("This test verifies that a user can log in and access his notes.")
@pytest.mark.api
def test_get_notes(token):
    response = get("https://practice.expandtesting.com/notes/api/notes/", token)
    assert response.status_code == 200
    assert "data" in response.json()
@allure.story("new user has no notes")
@allure.description("This test verifies that a new user has no notes.")
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
@allure.story("deleting note via api")
@allure.description("This test verifies that a note can be deleted successfully via the API.")
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
#TC-15 response times for /api/notes/ endpoint should be within 2s.
@allure.feature("NOTES MANAGEMENT API")
@allure.story("api response time within 2s")
@allure.description("This test verifies that the response time for the /api/notes/ endpoint is within 2 seconds.")
@pytest.mark.api.flaky(reruns=3, reruns_delay=5)
def test_notes_api_response_time(token):
    start_time = time.time()
    response = get("https://practice.expandtesting.com/notes/api/notes/", token)
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 2, f"API response time was {(end_time - start_time)} seconds, which is longer than the expected 2 seconds."
@allure.story("api post response time within 2s")
@allure.description("This test verifies that the response time for the POST /notes/ endpoint is within 2 seconds and returns correct data.")
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
@allure.story("api delete response time within 2s")
@allure.description("This test verifies that the response time for the DELETE /notes/{id} endpoint is within 2 seconds and returns correct status code.")
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
@allure.story("api get notes unauthorized access")
@allure.description("This test verifies that the GET /notes/ endpoint returns status code 404 on unauthorized access.")
@pytest.mark.api
def test_get_notes_unauthorized():
    response = get("https://practice.expandtesting.com/notes/api/notes/", token=None)
    assert response.status_code == 401, f"Expected status code 401 for unauthorized access, but got {response.status_code}."
#TC-21 get note with invalid token
@allure.feature("NOTES MANAGEMENT API")
@allure.story("get notes with invalid token")
@allure.description("This test verifies that the GET /notes/ endpoint returns status code 401 for invalid token.")
@pytest.mark.api
def test_get_notes_invalid_token():
    invalid_token = "invalid_token_example"
    response = get("https://practice.expandtesting.com/notes/api/notes/", token=
invalid_token)
    assert response.status_code == 401, f"Expected status code 401 for invalid token, but got {response.status_code}."
#TC-22 deleting note with invalid token 
@allure.feature("NOTES MANAGEMENT API")
@allure.story("delete notes with invalid token")
@allure.description("This test verifies that the DELETE /notes/{id} endpoint returns status code 401 for invalid token.")
@pytest.mark.api
def test_delete_note_invalid_token():
    invalid_token = "invalid_token_example"
    create_response = create_note_api(invalid_token, "Test_Note", "This is a test note.", "Work", False)
    assert create_response.status_code == 401, f"Expected status code 401 for invalid token during note creation, but got {create_response.status_code}."

