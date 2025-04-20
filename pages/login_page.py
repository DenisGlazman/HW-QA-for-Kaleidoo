from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.get_by_role("textbox", name="שם משתמש או כתובת אימייל").fill(username)
        self.page.get_by_role("textbox", name="סיסמא").fill(password)
        self.page.get_by_role("button", name="התחברות").click()
