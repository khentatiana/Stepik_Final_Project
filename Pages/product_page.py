from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def go_to_product_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()


    # this methods will be called in test_product_page.py
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "ADD_TO_BASKET button IS NOT PRESENTED"


    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_success_message(self):
        has_been_added_message = self.browser.find_element(By.XPATH, "//div[@id='messages']//div[1]//div[1]")
        has_been_added_message.is_displayed()

    def should_be_present_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "PRODUCT_NAME button IS NOT PRESENT"
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "no ALERT_ADDED_TO_CART"





