import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Cart:
    def __init__(self, driver):
        self.driver = driver


    checkout = (By.ID, "checkout")


    def check_out(self):
        return self.driver.find_element(*Cart.checkout)
