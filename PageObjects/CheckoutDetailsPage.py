import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class CheckoutDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.ID, "first-name")
    lastName = (By.ID, "last-name")
    postalCode = (By.ID, "postal-code")
    continueButton = (By.ID, "continue")

    def first_name(self):
        return self.driver.find_element(*CheckoutDetailsPage.firstName)

    def last_name(self):
        return self.driver.find_element(*CheckoutDetailsPage.lastName)

    def postal_code(self):
        return self.driver.find_element(*CheckoutDetailsPage.postalCode)

    def continue_button(self):
        return self.driver.find_element(*CheckoutDetailsPage.continueButton)

