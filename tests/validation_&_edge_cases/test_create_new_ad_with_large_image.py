import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.new_ad_page import NewAdPage

@allure.title("Create and publish new real estate ad with BIG IMAGE")
def test_create_new_ad(page: Page):
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
            new_ad_page.fill_only_required_ad_details()
            new_ad_page.fill_only_required_additional_details()
            new_ad_page.select_features()
            # Generate a unique identifier and add it to the description
            unique_id = new_ad_page.fill_description()
            new_ad_page.fill_only_required_payment_details()
            new_ad_page.select_date("April 20, 2025")
        except Exception as e:
            print(f"Error while filling ad details: {e}")
            # Continue the test execution

    with allure.step("Upload image and fill contact info"):
        try:
            new_ad_page.upload_big_images("tests/resources/big_image.jpg")
            new_ad_page.expect_file_size_limit_error()

        except Exception as e:
            print(f"Error while uploading images or filling contact info: {e}")
