from.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    # this methods will be called in test_product_page.py
    def should_be_add_to_cart_button(self):
        add_to_basket = self. browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        add_to_basket.is_displayed()

    def add_product_to_cart(self):
        add_to_basket = self.browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        add_to_basket.click()

    def should_be_success_message(self):
        has_been_added_message = self.browser.find_element(By.XPATH, "//div[@id='messages']//div[1]//div[1]")
        has_been_added_message.is_displayed()




