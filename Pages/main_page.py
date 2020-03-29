from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):

    # this methods will be called in test_main_page.py
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    # this methods will be called in test_main_page.py. This method purposely using wrong locator.
    # If you change locator to correct one: "login_link", then test will pass
    # def should_be_login_link(self):
    #     assert self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid_locator"), \
    #         "Login link is not presented"
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid_locator"), \
    #         "Login link IS NOT PRESENT"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link IS NOT PRESENTED"
