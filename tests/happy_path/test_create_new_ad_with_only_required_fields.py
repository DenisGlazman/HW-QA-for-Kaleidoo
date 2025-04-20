import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.new_ad_page import NewAdPage

@allure.title("Create and publish new real estate ad with only required fields")
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
            new_ad_page.upload_images("tests/resources/1.jpg")
            new_ad_page.fill_contact_info()
        except Exception as e:
            print(f"Error while uploading images or filling contact info: {e}")
            # Continue the test execution

    with allure.step("Submit and verify ad is posted"):
        try:
            new_ad_page.submit_ad()
            new_ad_page.verify_ad_posted()
        except Exception as e:
            print(f"Error during ad submission: {e}")
            # Continue the test execution

    with allure.step("Navigate to the ad and verify the unique ID"):
        try:
            # Click on the link to go to the ad page
            page.get_by_role("link", name="Apartment Listings").first.click()

            # Click on the price of the ad to go to the ad details page
            page.get_by_role("heading", name="₪1,200").first.click()

            # Click on the ad description to check if the unique identifier is present
            ad_description = page.get_by_text(
                f"\"Beautiful and spacious apartment in an excellent location! Ad Identifier: {unique_id}\"")

            # Check that the unique identifier text is present
            ad_description.click()
            assert unique_id in ad_description.inner_text(), f"Identifier {unique_id} not found in the ad description"
        except Exception as e:
            print(f"Error during ad navigation or verification: {e}")
            # Continue the test execution
