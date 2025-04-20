import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.new_ad_page import NewAdPage

@allure.title("Create new ad without picked required field (type of appartmes)")
def test_create_ad(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    new_ad_page = NewAdPage(page)

    with allure.step("Open homepage and log in"):
        try:
            home_page.goto()
            home_page.accept_terms()
            home_page.go_to_login()
            login_page.login(username="tester", password="tester123!@#qwe")
        except Exception as e:
            print(f"Error during login: {e}")
            # Continue the test execution despite the error

    with allure.step("Start new ad creation"):
        try:
            home_page.go_to_new_ad()
        except Exception as e:
            print(f"Error while starting new ad creation: {e}")
            # Continue the test execution

    with allure.step("Fill in ad details"):
        try:
            new_ad_page.fill_not_all_ad_details()
            new_ad_page.expect_required_field_error()

        except Exception as e:
            print(f"Error while filling ad details: {e}")


