import os
import pytest
from pages.login_page import LoginPage

def test_access_protected_route_without_authentication(page):
    login_page = LoginPage(page)
    page.goto(f"{login_page.base_url}/dashboard")
    page.wait_for_load_state('networkidle')
    assert "/sign-in" in page.url