import os
import pytest
from pages.login_page import LoginPage

def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    page.goto(f"{login_page.base_url}/sign-in")
    login_page.login("invalid@example.com", "wrongpass")
    assert "Incorrect email or password" in login_page.get_error_message()