import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class FinishShopping:
    def __init__(self, driver):
        self.driver = driver

    finishSHopping = (By.ID, "finish")

    def finish_shopping(self):
        return self.driver.find_element(*FinishShopping.finishSHopping)
