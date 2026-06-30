import pytest
import allure
from fixtures.auth_client import *
from utils.logger import get_logger
import allure
logger = get_logger(__name__)
@allure.feature("LOGIN API")
@allure.story("api login")
@pytest.mark.api
def test_login_api():
    response = post("https://practice.expandtesting.com/notes/api/users/login", {"email": "saiviveksapelly@gmail.com", "password": "142536475869"})
    assert response.status_code == 200
    assert "data" in response.json()
    assert "token" in response.json()["data"]
