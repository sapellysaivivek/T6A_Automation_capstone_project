from pages.Base_Page import BasePage
from selenium.webdriver.common.by import By
import allure
class LoginPage(BasePage):
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Login_Option = (By.XPATH, "//a[@href='/notes/app/login']")
    Login_Button = (By.XPATH, "//button[text()='Login']")
    def click_login_option(self):
        with allure.step("Clicking on the 'Login' option to navigate to the login page"):
            self.click(self.Login_Option)
    def click_login_button(self):
        with allure.step("Clicking on the 'Login' button"):
            self.click(self.Login_Button)
    def enter_email(self, email):
        with allure.step("Entering email in the email input field"):
            self.send_keys(self.Email, email)
    def enter_password(self, password):
        with allure.step("Entering password in the password input field"):
            self.send_keys(self.Password, password)
    def click_login(self, email, password):
        with allure.step("Attempting to log in"):
            self.click_login_option()
            self.enter_email(email)
            self.enter_password(password)
            self.click_login_button()
      
