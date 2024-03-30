import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class ShoppingPage:
    def __init__(self, driver):
        self.driver = driver

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    bikeLight = (By.ID, "add-to-cart-sauce-labs-bike-light")
    boltTShirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    fleece = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    allThingsTShirt = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    viewCart = (By.ID, "shopping_cart_container")

    def add_items1_to_cart(self):
        return self.driver.find_element(*ShoppingPage.backpack)

    def add_items2_to_cart(self):
        return self.driver.find_element(*ShoppingPage.bikeLight)

    def add_items3_to_cart(self):
        return self.driver.find_element(*ShoppingPage.boltTShirt)

    def add_items4_to_cart(self):
        return self.driver.find_element(*ShoppingPage.fleece)

    def add_items5_to_cart(self):
        return self.driver.find_element(*ShoppingPage.onesie)

    def add_items6_to_cart(self):
        return self.driver.find_element(*ShoppingPage.allThingsTShirt)

    def view_shopping_cart(self):
        return self.driver.find_element(*ShoppingPage.viewCart)
