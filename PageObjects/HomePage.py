import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Homepage:
    def __init__(self, driver):
        self.driver = driver

    appName = (By.CLASS_NAME, "app_logo")
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def app_name(self):
        return self.driver.find_elements(*Homepage.appName)

    def get_username(self):
        return self.driver.find_element(*Homepage.username)

    def get_password(self):
        return self.driver.find_element(*Homepage.password)

    def get_login_button(self):
        return self.driver.find_element(*Homepage.login_button)
