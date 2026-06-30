from selenium.webdriver.common.by import By
import allure
from pages.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    Add_Notes_Button = (By.XPATH,"//button[text()='+ Add Note']")

    Create_Button = (By.XPATH,"//button[text()='Create']")

    Cancel_Button = (By.XPATH,"//button[@data-testid='note-cancel']")

    Category_Dropdown = (By.ID,"category")

    Completed_Checkbox = (By.ID,"completed")

    Title_Input = (By.ID,"title")

    Description_Input = (By.ID,"description")

    # NOTES
    Note_Title = (By.XPATH,"//div[contains(@class,'card')]//h5")

    Delete_Button = (By.XPATH,"//button[contains(text(),'Delete')]")

    Edit_Button = (By.XPATH,"//button[contains(text(),'Edit')]")


    def click_add_notes(self):
        with allure.step("Clicking on the 'Add Note' button"):

            self.click(self.Add_Notes_Button)


    def select_category(self, category):
        with allure.step(f"Selecting category '{category}' from the dropdown"):

            self.select_dropdown(
                self.Category_Dropdown,
                category
            )


    def enter_title(self, title):
        with allure.step(f"Entering title '{title}' in the title input field"):
            self.send_keys(
                self.Title_Input,
                title
            )


    def enter_description(self, description):
        with allure.step(f"Entering description '{description}' in the description input field"):
            self.send_keys(
                self.Description_Input,
                description
            )


    def mark_completed(self):
        with allure.step("Marking the note as completed by checking the checkbox"):

            self.check_checkbox(
                self.Completed_Checkbox
            )

  
    def click_create(self):
        with allure.step("Clicking on the 'Create' button to create the note"):
            self.click(
                self.Create_Button
            )


    def click_cancel(self):
        with allure.step("Clicking on the 'Cancel' button to cancel the note creation"):
            self.click(
                self.Cancel_Button
            )

    def create_note(self,category,title,description,completed=False):
        with allure.step(f"Creating a new note with title '{title}', category '{category}', and completed status '{completed}'"):
            self.click_add_notes()

            self.select_category(category)

            self.enter_title(title)

            self.enter_description(description)

            if completed:

                self.mark_completed()

            self.click_create()

    def is_note_visible(self, title):
        with allure.step(f"Checking if the note with title '{title}' is visible on the page"):
            locator = (
            By.XPATH,
            f"//h5[text()='{title}']"
        )

        return self.is_visible(locator)

        

    


    def delete_note(self, title):
        with allure.step(f"Deleting the note with title '{title}'"):
            self.click((
                By.XPATH,
                f"//div[@data-testid='note-card-title' and text()='{title}']"
                f"/ancestor::div[@data-testid='note-card']"
                f"//button[@data-testid='note-delete']"
            ))

            self.click((
                By.XPATH,
                "//button[@data-testid='note-delete-confirm']"
            ))

        


    def click_edit_note(self, title):
        with allure.step(f"Clicking the 'Edit' button for the note with title '{title}'"):
            edit_locator = (
                By.XPATH,
                f"//h5[text()='{title}']/ancestor::div[contains(@class,'card')]//button[contains(text(),'Edit')]"
            )

            self.click(edit_locator)
    def mark_note_as_completed(self, title):
        with allure.step(f"Marking the note with title '{title}' as completed by checking the checkbox"):
            checkbox_locator = (
                By.XPATH,
                f"//div[@data-testid='note-card-title' and text()='{title}']"
                f"/ancestor::div[@data-testid='note-card']"
                f"//input[@type='checkbox']"
            )

            self.check_checkbox(checkbox_locator)
        