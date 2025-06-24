from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "[data-hook='sign-in-email-input']"
        self.password_input = "[data-hook='sign-in-password-input']"
        self.login_button = "[data-hook='sign-in-submit-button']"

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)