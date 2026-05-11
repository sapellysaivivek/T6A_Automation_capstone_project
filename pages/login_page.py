from pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Login_Option = (By.XPATH, "//a[@href='/notes/app/login']")
    Login_Button = (By.XPATH, "//button[text()='Login']")
    def click_login_option(self):
        self.click(self.Login_Option)
    def click_login_button(self):
        self.click(self.Login_Button)
    def enter_email(self, email):
        self.send_keys(self.Email, email)
    def enter_password(self, password):
        self.send_keys(self.Password, password)
    def click_login(self, email, password):
        self.click_login_option()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
      

    