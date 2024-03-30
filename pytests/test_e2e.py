from PageObjects.CheckoutDetailsPage import CheckoutDetailsPage
from PageObjects.FinishShopping import FinishShopping
from PageObjects.HomePage import Homepage
from PageObjects.ShoppingPage import ShoppingPage
from PageObjects.cart import Cart
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):
        homepage = Homepage(self.driver)
        homepage.get_username().send_keys('standard_user')
        homepage.get_password().send_keys('secret_sauce')
        homepage.get_login_button().click()

    def test_add_items_to_cart(self):
        shoppingpage = ShoppingPage(self.driver)
        shoppingpage.add_items1_to_cart().click()
        shoppingpage.add_items2_to_cart().click()
        shoppingpage.add_items3_to_cart().click()
        shoppingpage.add_items4_to_cart().click()
        shoppingpage.add_items5_to_cart().click()
        shoppingpage.add_items6_to_cart().click()
        shoppingpage.view_shopping_cart().click()

    def test_checkout(self):
        checkOut = Cart(self.driver)
        checkOut.check_out().click()

    def test_enter_checkout_details(self):
        checkoutDetails = CheckoutDetailsPage(self.driver)
        checkoutDetails.last_name().send_keys('eshhhhh')
        checkoutDetails.first_name().send_keys("yoooo")
        checkoutDetails.postal_code().send_keys('1233')
        checkoutDetails.continue_button().click()

    def test_finish_shopping(self):
        finishShopping = FinishShopping(self.driver)
        finishShopping.finish_shopping().click()

