from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        try:
            self.page.goto("https://homme.co.il/", wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print("Error loading page:", e)
            self.page.screenshot(path="screenshots/goto_error.png")
            raise

    def accept_terms(self):
        self.page.get_by_role("link", name="אני מסכים לתנאי השימוש באתר").click()

    def go_to_login(self):
        self.page.get_by_role("link", name="התחבר").click()

    def go_to_new_ad(self):
        self.page.get_by_role("link", name="פרסם מודעה").click()

    def go_to_appartments(self):
        self.page.get_by_role("link",name='מאגר דירות').click()
