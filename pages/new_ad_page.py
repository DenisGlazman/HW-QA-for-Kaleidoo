import os
import uuid
import re

from playwright.sync_api import Page, expect

class NewAdPage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_load(self):
        self.page.wait_for_load_state("load")

    def fill_ad_details(self):
        self.wait_for_load()
        self.page.locator("#ff_8_asset_type").select_option("דירה")
        self.page.locator("#ff_8_asset_status").select_option("חדש מקבלן (לא גרו בנכס)")
        self.page.locator("#ff_8_city").select_option("כרמיאל")
        self.page.locator("#ff_8_street_1").select_option("אדום החזה")
        self.page.get_by_role("textbox", name="מספר בניין / בית").fill("11/12")
        self.page.get_by_role("button", name="הבא").nth(0).click()

    def fill_only_required_ad_details(self):
        self.wait_for_load()
        self.page.locator("#ff_8_asset_type").select_option("דירה")
        self.page.locator("#ff_8_asset_status").select_option("חדש מקבלן (לא גרו בנכס)")
        self.page.locator("#ff_8_city").select_option("כרמיאל")
        self.page.locator("#ff_8_street_1").select_option("אדום החזה")
        self.page.get_by_role("button", name="הבא").nth(0).click()

    def fill_not_all_ad_details(self):
        self.wait_for_load()
        self.page.locator("#ff_8_asset_type").select_option("-------")
        self.page.locator("#ff_8_asset_status").select_option("חדש מקבלן (לא גרו בנכס)")
        self.page.locator("#ff_8_city").select_option("כרמיאל")
        self.page.locator("#ff_8_street_1").select_option("אדום החזה")
        self.page.get_by_role("button", name="הבא").nth(0).click()


    def fill_additional_details(self):
        self.wait_for_load()
        self.page.get_by_role("textbox", name="קומה").fill("3")
        self.page.get_by_role("textbox", name="מתוך").fill("5")
        self.page.locator("#ff_8_room_num").select_option("3")
        self.page.locator("#ff_8_terrace").select_option("3")
        self.page.locator("#ff_8__parking").select_option("1")
        self.page.get_by_role("textbox", name="מ\"ר בנוי").fill("100")
        self.page.get_by_role("textbox", name="מ\"ר גינה").fill("250")
        self.page.locator("#ff_8_elevator_1").select_option("ללא")
        self.page.get_by_role("button", name="הבא").nth(1).click()

    def fill_only_required_additional_details(self):
        self.wait_for_load()
        self.page.get_by_role("textbox", name="קומה").fill("3")
        self.page.locator("#ff_8_room_num").select_option("3")
        self.page.locator("#ff_8_terrace").select_option("3")
        self.page.locator("#ff_8__parking").select_option("1")
        self.page.get_by_role("textbox", name="מ\"ר בנוי").fill("100")
        self.page.locator("#ff_8_elevator_1").select_option("ללא")
        self.page.get_by_role("button", name="הבא").nth(1).click()

    def select_features(self):
        self.wait_for_load()
        self.page.get_by_label("ריהוט").first.click()
        self.page.get_by_role("button", name="הבא").nth(2).click()
        self.wait_for_load()

    def generate_unique_id(self):
        return str(uuid.uuid4())

    def fill_description(self, text="דירה יפה ומרווחת במיקום מצוין!"):
        unique_id = self.generate_unique_id()  # Generate a unique identifier
        description_with_id = f"{text} Ad ID: {unique_id}"
        description_field = self.page.locator("textarea[placeholder*='תאר את הנכס כאן']")
        description_field.fill(description_with_id)
        return unique_id  # Return the unique identifier for validation

    def fill_payment_details(self):
        self.wait_for_load()
        self.page.get_by_role("spinbutton", name="מספר תשלומים").fill("10")
        self.page.get_by_role("textbox", name="מחיר").fill("1200")
        self.page.get_by_role("textbox", name="ועד בית").click()
        self.page.get_by_role("textbox", name="ועד בית").fill("150")
        self.page.get_by_role("textbox", name="ארנונה לחודשיים").click()
        self.page.get_by_role("textbox", name="ארנונה לחודשיים").fill("800")

    def fill_only_required_payment_details(self):
        self.wait_for_load()
        self.page.get_by_role("spinbutton", name="מספר תשלומים").fill("10")
        self.page.get_by_role("textbox", name="מחיר").fill("1200")

    def select_date(self, date_label: str):
        self.wait_for_load()
        date_input = self.page.locator('input[name="date_start"]')
        date_input.wait_for(state="attached", timeout=10000)
        date_input.click()

        date_element = self.page.locator(f'span[aria-label="{date_label}"]')
        date_element.wait_for(state="visible", timeout=10000)
        date_element.click(force=True)

        # Wait until the value appears in the input field
        element_handle = date_input.element_handle()
        self.page.wait_for_function("el => el.value !== ''", arg=element_handle)

        selected_date = date_input.input_value()
        print(f"Selected date: {selected_date}")

        # Click the "Next" button
        next_button = self.page.get_by_role("button", name="הבא").nth(3)
        next_button.wait_for(state="visible", timeout=10000)
        next_button.click()

    def upload_images(self, file_name: str):
        self.wait_for_load()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, file_name)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

        print(f"Uploading from: {full_path}")
        file_input = self.page.locator('input[type="file"]')
        file_input.wait_for(timeout=60000)
        file_input.set_input_files(full_path, timeout=60000)

        # ⏳ Wait for the "100% Completed" text to appear
        progress_group = self.page.get_by_role("group")
        expect(progress_group).to_contain_text("100% Completed")

        # ✅ Click the "Next" button only after upload is complete
        self.page.get_by_role("button", name="הבא").nth(4).click()

    def upload_big_images(self, file_name: str):
        self.wait_for_load()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, file_name)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

        print(f"Uploading from: {full_path}")
        file_input = self.page.locator('input[type="file"]')
        file_input.wait_for(timeout=60000)
        file_input.set_input_files(full_path, timeout=60000)




    def fill_contact_info(self):
        self.wait_for_load()
        self.page.get_by_role("textbox", name="שם מלא *").click()
        self.page.get_by_role("textbox", name="שם מלא *").fill("Testuser1")
        self.page.get_by_role("textbox", name="מספר טלפון").click()
        self.page.get_by_role("textbox", name="מספר טלפון").fill("0501234567")

    def submit_ad(self):
        self.wait_for_load()
        # Locator for "Publish Property" button
        publish_button = self.page.locator("button:has-text('פרסום הנכס')")

        # Screenshot for debugging (to see what's rendered)
        self.page.screenshot(path="debug_submit_ad.png")
        print("Screenshot saved: debug_submit_ad.png")

        # Wait for the button to appear in the DOM (might be hidden)
        publish_button.wait_for(state="attached", timeout=10000)

        # Log the button's state
        is_visible = publish_button.is_visible()
        is_enabled = publish_button.is_enabled()
        print(f"'Publish' button — visible: {is_visible}, enabled: {is_enabled}")

        # If button is hidden — optionally wait manually
        if not is_visible:
            print("Waiting for the button to become visible...")
            self.page.wait_for_timeout(3000)  # wait 3 seconds
            self.page.screenshot(path="debug_submit_waited.png")
            is_visible = publish_button.is_visible()
            print(f"After waiting: visible = {is_visible}")

        # Click if ready
        if is_visible and is_enabled:
            publish_button.click()
            print("✅ Button clicked — ad submitted.")
        else:
            raise Exception("'Publish' button is inactive or hidden. Make sure all required fields are filled.")

    def verify_ad_posted(self):
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(2000)  # Replace with explicit wait for element if needed

        # Check confirmation heading or message
        expect(self.page.locator("h1")).to_contain_text("פרסום מודעה")

        # Check that the URL contains an ID or confirmation pattern
        expect(self.page).to_have_url(re.compile(".*(confirmation|success|ad/\\d+).*"))

        # Check for success message text (adjust to the actual site)
        confirmation = self.page.locator("text=המודעה פורסמה בהצלחה")
        expect(confirmation).to_be_visible()

        # Final page screenshot
        self.page.screenshot(path="screenshots/verify_ad_posted.png")

    def verify_unique_id_in_description(self, unique_id):
        description_text = self.page.locator("textarea[placeholder*='תאר את הנכס כאן']").inner_text()
        assert unique_id in description_text, f"Ad ID {unique_id} was not found in the description"

    def expect_file_size_limit_error(self):
        error_group = self.page.get_by_role("group")
        expect(error_group).to_contain_text("מגבלת גודל קובץ מקסימלית היא 5MB")

    def expect_required_field_error(self):
        error_group = self.page.get_by_role("group")
        expect(error_group).to_contain_text("זהו שדה חובה")
