from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # this methods will be called in test_product_page.py
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET),\
            "ADD_TO_BASKET button IS NOT PRESENTED"
        print("\nProductPage: ADD_TO_BASKET is present on web page ")

    def add_product_to_cart(self, promo=False):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        print("\nProductPage: ADD_TO_BASKET button is clicked ")

        if promo:
            self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).get_attribute("innerText")
        print("ProductPage: success_message is: " + success_message)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message NOT is disappeared, but should"

    def should_be_present_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME),\
            "ProductPage: PRODUCT_NAME button IS NOT PRESENT"
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), \
            "ProductPage: no ALERT_ADDED_TO_CART"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_CART)\
            .get_attribute("innerText") # store text of ALERT_ADDED_TO_CART, better to use .get_attribute("innerText")
                                        # and not .text
        print("ProductPage: Product name is " + alert_text)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).\
            get_attribute("innerText")  # store text of PRODUCT_NAME, better to use .get_attribute("innerText")
                                        # and not .text
        print("ProductPage: Product name is \"" + product_name + " \" ")
        assert alert_text in product_name, \
            f"ProductPage: The alert contains WRONG product name: {alert_text} - {product_name}"

    def should_check_total_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "ProductPage: PRODUCT_PRICE is not PRESENT"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS), \
            "ProductPage: no ALERT_CART_STATUS"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_CART_STATUS).text    # store text of ALERT_CART_STATUS
        product_total = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text  # store text of PRODUCT_PRICE
        assert product_total in alert_text, \
            f"ProductPage: Product cost in basket is not equal to product price.ALERT TEXT: {alert_text} and PRODUCT PRICE: {product_total}"









