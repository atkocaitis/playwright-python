import os
import pytest
from playwright.sync_api import sync_playwright

HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield page
        finally:
            context.close()
            browser.close()