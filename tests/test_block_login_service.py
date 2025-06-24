import os
import pytest
from pages.login_page import LoginPage

def test_block_login_service_response(page):
    login_page = LoginPage(page)
    page.route("**/api/proxy-bff/auth/v2/sign-in/local", lambda route: route.abort())
    page.goto(f"{login_page.base_url}/sign-in")
    login_page.login("test@example.com", "password")
    assert "An error occurred" in login_page.get_error_message()