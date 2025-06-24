import os
from playwright.sync_api import Page
from dotenv import load_dotenv
load_dotenv()

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        self.error_message = "[data-hook='sign-in-password-input-helper-text']"

    def get_error_message(self):
        self.page.locator(self.error_message).wait_for(state="visible")
        self.page.wait_for_load_state('networkidle')
        return self.page.locator(self.error_message).text_content()