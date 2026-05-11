from selenium.webdriver.common.by import By

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

        self.click(self.Add_Notes_Button)


    def select_category(self, category):

        self.select_dropdown(
            self.Category_Dropdown,
            category
        )


    def enter_title(self, title):

        self.send_keys(
            self.Title_Input,
            title
        )


    def enter_description(self, description):

        self.send_keys(
            self.Description_Input,
            description
        )


    def mark_completed(self):

        self.check_checkbox(
            self.Completed_Checkbox
        )

  
    def click_create(self):

        self.click(
            self.Create_Button
        )


    def click_cancel(self):

        self.click(
            self.Cancel_Button
        )

    def create_note(self,category,title,description,completed=False):

        self.click_add_notes()

        self.select_category(category)

        self.enter_title(title)

        self.enter_description(description)

        if completed:

            self.mark_completed()

        self.click_create()

    def is_note_visible(self, title):

        locator = (
            By.XPATH,
            f"//h5[text()='{title}']"
        )

        return self.is_visible(locator)

    


    def delete_note(self, title):

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

        edit_locator = (
            By.XPATH,
            f"//h5[text()='{title}']/ancestor::div[contains(@class,'card')]//button[contains(text(),'Edit')]"
        )

        self.click(edit_locator)
    def mark_note_as_completed(self, title):

        checkbox_locator = (
            By.XPATH,
            f"//div[@data-testid='note-card-title' and text()='{title}']"
            f"/ancestor::div[@data-testid='note-card']"
            f"//input[@type='checkbox']"
        )

        self.check_checkbox(checkbox_locator)